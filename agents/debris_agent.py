from langchain_core.runnables import RunnableLambda
import random

debris_agent = RunnableLambda(
    lambda state: {
        **state,
        "debris_risk": "High" if random.random() < 0.3 else "Low"
    }
)