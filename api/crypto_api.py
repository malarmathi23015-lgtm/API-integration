import requests
from config import CRYPTO_URL


def get_crypto_prices():

    params = {
        "ids": "bitcoin,ethereum,dogecoin",
        "vs_currencies": "usd"
    }

    try:
        response = requests.get(CRYPTO_URL, params=params)
        return response.json()

    except Exception as e:
        return {"error": str(e)}