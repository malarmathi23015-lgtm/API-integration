def detect_market_trend(prices):

    btc_price = prices["bitcoin"]["usd"]

    if btc_price > 65000:
        return "UPTREND"

    elif btc_price < 50000:
        return "DOWNTREND"

    return "STABLE"