import requests
from config import WEATHER_API_KEY, WEATHER_URL


def get_weather(city="Chennai"):
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(WEATHER_URL, params=params)
        data = response.json()

        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"]
        }

    except Exception as e:
        return {"error": str(e)}