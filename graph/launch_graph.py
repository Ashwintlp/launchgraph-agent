from typing import TypedDict
from langgraph.graph import StateGraph, END
from agents.weather_agent import weather_agent
from agents.nasa_agent import nasa_agent
from agents.debris_agent import debris_agent
from agents.recommendation_agent import recommendation_agent
from agents.decision_agent import decision_agent

class LaunchState(TypedDict):
    location: str
    weather: str
    solar_activity: str
    debris_risk: str
    recommendation: str
    decision: str

def build_launch_graph():
    builder = StateGraph(LaunchState)

    builder.add_node("weather", weather_agent)
    builder.add_node("nasa", nasa_agent)
    builder.add_node("debris", debris_agent)
    builder.add_node("recommendation", recommendation_agent)
    builder.add_node("decision", decision_agent)

    builder.set_entry_point("weather")
    builder.add_edge("weather", "nasa")
    builder.add_edge("nasa", "debris")
    builder.add_edge("debris", "recommendation")
    builder.add_edge("recommendation", "decision")
    builder.add_edge("decision", END)

    return builder.compile()