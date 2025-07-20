from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from models.schemas import LaunchQuery
from services.llm_service import analyze_launch, stream_analysis

router = APIRouter()
@router.post("/analyze-launch-request")
async def analyze_launch_request(query: LaunchQuery):
    return await analyze_launch(query.user_query)

@router.post("/stream-launch-analysis")
async def stream_launch(query: LaunchQuery):
    async def generate():
        async for chunk in stream_analysis(query.user_query):
            yield chunk
    return StreamingResponse(generate(), media_type="text/plain")