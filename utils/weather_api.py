import os, requests

def fetch_weather(location: str) -> str:
    key = os.getenv("OPENWEATHER_API_KEY", "")
    resp = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"q": location, "appid": key, "units": "metric"}
    )
    data = resp.json() if resp.ok else {}
    return data.get("weather", [{"main": "Unknown"}])[0]["main"]