from langchain_core.runnables import RunnableLambda
from utils.weather_api import fetch_weather

weather_agent = RunnableLambda(
    lambda state: {
        **state,
        "weather": fetch_weather(state["location"])
    }
)