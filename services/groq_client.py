import os
import json
import httpx
from dotenv import load_dotenv
from async_lru import alru_cache
from tenacity import retry, stop_after_attempt, wait_fixed

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama3-8b-8192"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
@alru_cache(maxsize=128)
async def get_llm_response(prompt: str) -> dict:
    payload = {
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(GROQ_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()

async def stream_llm_response(prompt: str):
    payload = {
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": True
    }
    async with httpx.AsyncClient() as client:
        async with client.stream("POST", GROQ_API_URL, headers=headers, json=payload) as response:
            async for line in response.aiter_lines():
                if line.startswith("data: "):
                    data = line[6:]
                    if data == "[DONE]":
                        break
                    chunk = json.loads(data)
                    yield chunk["choices"][0]["delta"].get("content", "")
