from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
from graph.launch_graph import build_launch_graph

load_dotenv()

app = FastAPI(title="Launch Decision API", version="1.0")

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
