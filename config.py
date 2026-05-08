import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
NEWS_URL = "https://newsapi.org/v2/top-headlines"
CRYPTO_URL = "https://api.coingecko.com/api/v3/simple/price"