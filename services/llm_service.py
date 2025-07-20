import json
import asyncio
import httpx
import os
from tenacity import retry, wait_exponential, stop_after_attempt
from services.cache import async_cache_get, async_cache_set
from utils.token_utils import chunk_text
from dotenv import load_dotenv
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletionChunk

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
@retry(wait=wait_exponential(min=1, max=10), stop=stop_after_attempt(3))
async def call_llm(prompt: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )
    return response.choices[0].message.content

async def analyze_launch(user_query: str):
    cached = await async_cache_get(user_query)
    if cached:
        return cached

    chunks = chunk_text(user_query)

    results = []
    for chunk in chunks:
        prompt = f"""
        You are a launch assistant. Extract structured fields from the input text and respond as JSON:
        - intent: [launch_request, delay_check, weather_inquiry, etc.]
        - location: launch site or region
        - timeframe: time window (date, 'this weekend', etc.)
        - concerns: list of user concerns (weather, solar flares, debris, etc.)
        - decision: [Safe, Caution, Unsafe]
        - explanation: short reasoning

        Input: "{chunk}"
        Output:
        """
        try:
            output = await call_llm(prompt)
            results.append(output)
        except Exception as e:
            results.append(f"Error: {str(e)}")

    final_result = results[0] if len(results) == 1 else " ".join(results)

    try:
        parsed = json.loads(final_result)
    except Exception:
        parsed = {"error": "Failed to parse LLM response", "raw": final_result}

    await async_cache_set(user_query, parsed)
    return parsed

async def stream_analysis(user_query: str):
    prompt = f"""
    You are a launch assistant. Extract structured fields from the input text and respond as JSON.
    Input: "{user_query}"
    Output:
    """

    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    async for chunk in response:
        if isinstance(chunk, ChatCompletionChunk):
            yield chunk.choices[0].delta.content or ""