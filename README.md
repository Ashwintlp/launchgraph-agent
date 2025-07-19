# rocket_launch_agent/README.md
# 🚀 LaunchGraph Agent

This is an agentic system built with [LangGraph](https://github.com/langchain-ai/langgraph) that simulates satellite launch window optimization using real-time data from NASA, Open Meteo, and Celestrak.

## 🌍 Features
- Weather forecasting from Open Meteo
- Solar flare activity check using NASA's DONKI API
- Orbital debris detection via Celestrak TLE
- LangGraph-based decision graph (GO / NO-GO)
- Intelligent launch window suggestion

## 📦 Project Structure
```
rocket_launch_agent/
├── main.py                      # Entry point
├── .env                         # Your NASA API key
├── agents/                     
│   ├── weather_agent.py         # Weather condition analysis
│   ├── nasa_agent.py            # Solar flare activity via NASA
│   ├── debris_checker.py        # Debris risk checker
│   ├── decision_agent.py        # GO / NO-GO logic
│   └── recommendation_agent.py # Suggest new launch time if NO-GO
├── graph/
│   └── launch_graph.py          # LangGraph pipeline setup
└── README.md
```

## 🛠️ Setup
1. **Clone repo**
```bash
git clone https://github.com/yourname/launchgraph-agent.git
cd launchgraph-agent
```

2. **Install dependencies**
```bash
pip install langgraph langchain requests python-dotenv
```

3. **Configure your `.env` file**
```env
NASA_API_KEY=your_actual_key_here
```

4. **Run the agent**
```bash
python main.py
```

## ✅ Sample Output
```bash
Final Decision: {'decision': 'NO_GO', 'new_recommendation': '2025-07-22T15:00:00+00:00'}
```

## 🛰️ Data Sources
- [NASA APIs](https://api.nasa.gov/)
- [Open Meteo](https://open-meteo.com/)
- [Celestrak TLE](https://celestrak.org/NORAD/elements/)

## 📖 License
MIT

---
Crafted for experimentation and fun with LangGraph and real-world space data. 🌌

inputs from swagger

{
"location": "Cape Canaveral",
"weather": "Clear",
"solar_activity": "Low",
"debris_risk": "Low"
}

result = graph.invoke({
    "location": "Cape Canaveral",
    "weather": "Clear",
    "solar_activity": "Low",
    "debris_risk": "Low"
 })
result = graph.invoke({
     "location": "Cape Canaveral",
     "weather": "Stormy",
     "solar_activity": "Low",
     "debris_risk": "Low"
 })
 result = graph.invoke({
     "location": "Vandenberg",
     "weather": "Clear",
     "solar_activity": "High",
     "debris_risk": "Low"
 })
result = graph.invoke({
    "location": "Kennedy Space Center",
    "weather": "Clear",
    "solar_activity": "Low",
    "debris_risk": "High"
})