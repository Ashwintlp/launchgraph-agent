from langchain_core.runnables import RunnableLambda

decision_agent = RunnableLambda(
    lambda state: {**state, "decision": state["recommendation"]}
)