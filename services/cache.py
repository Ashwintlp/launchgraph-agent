import asyncio

cache = {}

async def async_cache_get(key):
    return cache.get(key)

async def async_cache_set(key, value):
    cache[key] = value