from api.weather_api import get_weather
from api.crypto_api import get_crypto_prices
from api.news_api import get_news

from ai.sentiment import analyze_sentiment
from ai.trend_detector import detect_market_trend

from database.db import initialize_database, save_news

from alerts.alert_manager import check_crypto_alert


def main():

    initialize_database()

    print("\n===== WEATHER =====")
    weather = get_weather()
    print(weather)

    print("\n===== CRYPTO =====")
    crypto = get_crypto_prices()
    print(crypto)

    trend = detect_market_trend(crypto)

    print("\nMarket Trend:", trend)

    check_crypto_alert(crypto)

    print("\n===== NEWS =====")

    news_articles = get_news()

    for article in news_articles[:5]:

        title = article["title"]

        sentiment = analyze_sentiment(title)

        print(f"\nTitle: {title}")
        print("Sentiment:", sentiment)

        save_news(title, sentiment)


if __name__ == "__main__":
    main()