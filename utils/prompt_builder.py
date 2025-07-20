def build_prompt(user_query):
    prompt = f"""
You are a launch assistant. Only respond with a valid JSON object, no explanations or markdown. Extract the following structured fields from the user input:

- intent: [launch_request, delay_check, weather_inquiry, etc.]
- location: launch site or region
- timeframe: time window (date, 'this weekend', etc.)
- concerns: list of user concerns (weather, solar flares, debris, etc.)
- decision: [Safe, Caution, Unsafe]
- explanation: short reasoning

Input: "{user_query}"

Respond with ONLY a JSON object.
"""
    return prompt