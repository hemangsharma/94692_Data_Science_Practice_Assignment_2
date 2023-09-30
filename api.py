import requests

BASE_URL = "https://www.frankfurter.app/"

def fetch_currencies():
    response = requests.get(BASE_URL + "currencies")
    currencies = response.json()
    return currencies

def fetch_latest_rate(from_currency, to_currency):
    response = requests.get(BASE_URL + f"latest?amount=1&from={from_currency}&to={to_currency}")
    data = response.json()
    
    if to_currency not in data.get("rates", {}):
        return None
    
    return data["rates"][to_currency]

def fetch_historical_rate(from_currency, to_currency, date):
    response = requests.get(BASE_URL + f"{date}?amount=1&from={from_currency}&to={to_currency}")
    data = response.json()
    
    if to_currency not in data.get("rates", {}):
        return None
    
    return data["rates"][to_currency]
