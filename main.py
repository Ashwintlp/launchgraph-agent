from dotenv import load_dotenv
from graph.launch_graph import build_launch_graph

def main():
    load_dotenv()
    graph = build_launch_graph()
    # result = graph.invoke({
    #     "location": "Cape Canaveral",
    #     "weather": "Clear",
    #     "solar_activity": "Low",
    #     "debris_risk": "Low"
    # })
    # result = graph.invoke({
    #     "location": "Cape Canaveral",
    #     "weather": "Stormy",
    #     "solar_activity": "Low",
    #     "debris_risk": "Low"
    # })
    # result = graph.invoke({
    #     "location": "Vandenberg",
    #     "weather": "Clear",
    #     "solar_activity": "High",
    #     "debris_risk": "Low"
    # })
    result = graph.invoke({
        "location": "Kennedy Space Center",
        "weather": "Clear",
        "solar_activity": "Low",
        "debris_risk": "High"
    })

    print("Final Launch Decision:")
    print(result)

if __name__ == "__main__":
    main()