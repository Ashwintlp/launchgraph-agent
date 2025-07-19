from langchain_core.runnables import RunnableLambda
from utils.nasa_api import fetch_solar_activity

nasa_agent = RunnableLambda(
    lambda state: {
        **state,
        "solar_activity": fetch_solar_activity()
    }
)