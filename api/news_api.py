import requests
from config import NEWS_API_KEY, NEWS_URL


def get_news(category="technology"):

    params = {
        "country": "us",
        "category": category,
        "apiKey": NEWS_API_KEY
    }

    try:
        response = requests.get(NEWS_URL, params=params)
        data = response.json()

        return data.get("articles", [])

    except Exception as e:
        return [{"error": str(e)}]