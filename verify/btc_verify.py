import requests


def get_btc_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": "bitcoin", "vs_currencies": "usd"}
        res = requests.get(url, params=params, timeout=10)
        data = res.json()
        return data["bitcoin"]["usd"]
    except Exception:
        return None


def verify_direction(prediction, prev_price, current_price):
    if prev_price is None or current_price is None:
        return None

    p = prediction.lower()

    if "rise" in p or "up" in p:
        return current_price > prev_price

    if "fall" in p or "down" in p:
        return current_price < prev_price

    return None
