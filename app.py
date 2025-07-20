import json
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
from graph.launch_graph import build_launch_graph
from api import router_api
from fastapi.responses import StreamingResponse, JSONResponse
from services.groq_client import get_llm_response, stream_llm_response
from models.schemas import LaunchQuery
from utils.prompt_builder import build_prompt
load_dotenv()

app = FastAPI(title="Launch Decision API", version="1.0")
app.include_router(router_api.router)

launch_graph = build_launch_graph()

class LaunchInput(BaseModel):
    location: str
    weather: Optional[str] = None
    solar_activity: Optional[str] = None
    debris_risk: Optional[str] = None

@app.post("/launch-decision")
def get_launch_decision(input_data: LaunchInput):
    input_dict = {
        "location": input_data.location
    }

    if input_data.weather:
        input_dict["weather"] = input_data.weather
    if input_data.solar_activity:
        input_dict["solar_activity"] = input_data.solar_activity
    if input_data.debris_risk:
        input_dict["debris_risk"] = input_data.debris_risk

    result = launch_graph.invoke(input_dict)
    return {"input": input_dict, "launch_decision": result}

@app.post("/analyze-launch-request-astream")
async def analyze_launch(query: LaunchQuery):
    prompt = build_prompt(query.user_query)

    try:
        response = await get_llm_response(prompt)
        content = response["choices"][0]["message"]["content"].strip()

        print("LLM Response Content:", content)

        # Safe parse
        try:
            json_data = json.loads(content)
        except json.JSONDecodeError:
            # Try to extract valid JSON if wrapped in markdown or extra text
            import re
            match = re.search(r"{[\s\S]*}", content)
            if match:
                json_data = json.loads(match.group(0))
            else:
                raise Exception("LLM response is not valid JSON")

        return JSONResponse(content=json_data)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/workflow-launch-analysis")
async def stream_launch_analysis(query: LaunchQuery):
    prompt = build_prompt(query.user_query)
    async def generate():
        async for chunk in stream_llm_response(prompt):
            yield chunk

    return StreamingResponse(generate(), media_type="text/plain")
