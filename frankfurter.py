from api import get_url
import json

BASE_URL = "https://api.frankfurter.app"

def get_currencies_list():
    url = f"{BASE_URL}/currencies"
    status_code, content = get_url(url)

    if status_code == 200:
        currencies = json.loads(content)
        return list(currencies.keys())
    else:
        return None

def get_latest_rates(from_currency, to_currency, amount):
    url = f"{BASE_URL}/latest?from={from_currency}&to={to_currency}&amount={amount}"
    status_code, content = get_url(url)

    if status_code == 200:
        data = json.loads(content)
        date = data.get("date")
        rate = data.get("rates", {}).get(to_currency)
        return date, rate
    else:
        return None, None

def get_historical_rate(from_currency, to_currency, from_date, amount):
    url = f"{BASE_URL}/{from_date}?from={from_currency}&to={to_currency}&amount={amount}"
    status_code, content = get_url(url)

    if status_code == 200:
        data = json.loads(content)
        rate = data.get("rates", {}).get(to_currency)
        return rate
    else:
        return None
