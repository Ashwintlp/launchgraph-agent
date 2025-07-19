from langchain_core.runnables import RunnableLambda

def rec_fn(state):
    w = state["weather"]
    s = state["solar_activity"]
    d = state["debris_risk"]
    if w == "Clear" and s == "Low" and d == "Low":
        msg = "All clear for launch."
    else:
        msg = "Conditions not safe for launch."
    return {**state, "recommendation": msg}

recommendation_agent = RunnableLambda(rec_fn)