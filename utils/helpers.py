def parse_weather_response(data):
    wind_speed = data.get("wind", {}).get("speed", 0)
    cloud_cover = data.get("clouds", {}).get("all", 0)
    is_clear = wind_speed < 10 and cloud_cover < 50
    return {
        "weather_ok": is_clear,
        "condition": f"Wind: {wind_speed} m/s, Clouds: {cloud_cover}%"
    }

def map_launch_site_to_coords(site):
    location_map = {
        "Cape Canaveral": {"lat": 28.3922, "lon": -80.6077},
        "Vandenberg": {"lat": 34.742, "lon": -120.5724},
    }
    return location_map.get(site)