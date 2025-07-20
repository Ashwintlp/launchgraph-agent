from pydantic import BaseModel

class LaunchQuery(BaseModel):
    user_query: str