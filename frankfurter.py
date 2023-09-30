import requests
import json

BASE_URL = "https://www.frankfurter.app/"

def fetch_currencies():
    response = requests.get(BASE_URL + "currencies")
    currencies = response.json()
    return currencies

def fetch_latest_rates():
    response = requests.get(BASE_URL + "latest")
    rates_data = response.json()
    return rates_data

def fetch_historical_rates(date):
    response = requests.get(BASE_URL + date)
    rates_data = response.json()
    return rates_data

if __name__ == "__main__":
    # Fetch and store currencies
    currencies = fetch_currencies()
    with open("currencies.json", "w") as f:
        json.dump(currencies, f)

    # Fetch and store latest rates
    latest_rates = fetch_latest_rates()
    with open("latest_rates.json", "w") as f:
        json.dump(latest_rates, f)

    # Fetch and store historical rates for a specific date
    date = "2023-09-29"
    historical_rates = fetch_historical_rates(date)
    with open(f"historical_rates_{date}.json", "w") as f:
        json.dump(historical_rates, f)
