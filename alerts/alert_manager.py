def check_crypto_alert(prices):

    btc_price = prices["bitcoin"]["usd"]

    if btc_price < 50000:
        print("ALERT: Bitcoin crashed below $50,000")