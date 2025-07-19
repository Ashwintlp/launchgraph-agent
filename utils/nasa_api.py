import os, requests

def fetch_solar_activity() -> str:
    key = os.getenv("NASA_API_KEY", "")
    resp = requests.get(
        "https://api.nasa.gov/DONKI/FLR",
        params={"startDate": "2025-01-01", "endDate": "2025-12-31", "api_key": key}
    )
    data = resp.json() if resp.ok else []
    return "High" if data else "Low"