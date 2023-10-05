# Building Currency Converter in Python #

## Author
<h3>Name: Hemang Sharma <br>
Student ID: 24695785</h3>

## Description

**Currency Converter** is a Python web application that allows users to convert between different currencies. This application leverages the Frankfurter API to fetch the latest exchange rates and historical rates for various currencies.

### Features

- Users can enter the amount they want to convert.
- Users can select the source currency and target currency from dropdown menus.
- Users can choose a specific historical date for currency conversion.
- The application calculates the converted amount based on the selected currencies and date.
- It provides information about the conversion rate and the inverse rate.
- The conversion result is displayed in a user-friendly format.

### Challenges

Some of the challenges faced during the development of this project include:

- Integrating external APIs and handling API responses.
- Implementing proper error handling for API calls.
- Formatting and displaying the conversion result in a user-friendly way.
- Managing date input and conversion logic for historical rates.

### Future Features

In the future, the Currency Converter web application could be enhanced with the following features:

- User authentication and profiles to save conversion history.
- Support for a wider range of currencies.
- Real-time currency conversion updates.
- Currency exchange rate trend analysis.
- Mobile application version for convenience on the go.

The project aims to provide users with a reliable and user-friendly tool for currency conversion while continuously improving and expanding its functionality.

## How to Setup
### Prerequisites
- Python 3.10.10
- pip 23.0.1

### Python packages:
- Streamlit
- Requests
- Datetime
- JSON

## How to Run the Program


1. Navigate to your project folder:
`cd myproject`
2. Create a new virtual environment in that folder and activate that environment:
`python -m venv .venv`
3. Install Streamlit in your environment:
`pip install streamlit`
4. Test that the installation worked:
`streamlit hello`
5. In order to run this program, type `streamlit run app.py` in the terminal.

## Project Structure

The project consists of the following files:

1. app.py: The main Streamlit script for user input and displaying results.
2. api.py: Contains code for making API calls.
3. frankfurter.py: Includes functions for fetching exchange rate data from the Frankfurter API.
4. currency.py: Contains functions for formatting results to be displayed in the Streamlit app.
5. README.md: a markdown file containing listing of all Python functions and instructions for running the web app

### Functions Used
1. **api.py**:
    - `get_url(url)`: This function takes a URL as input and performs a GET request to that URL using the requests library. It attempts to fetch data from the provided URL. If the request is successful, it returns a tuple containing two values:
     - status_code: The HTTP status code of the response.
     - content: The content of the HTTP response as a string.
    If the GET request encounters an error, such as a network issue or an invalid URL, it catches the requests.exceptions.RequestException exception and handles it. In this case, it returns None, None to indicate an error occurred and prints an error message.

2. **app.py**:
    - `get_currencies_list()`: This function calls an API endpoint to fetch a list of available currencies from the Frankfurter API. It performs a check to see if the API call was successful and returns the list of currency codes as a Python list if successful, or None in case of an error.
    - `get_latest_rates(from_currency, to_currency, amount)`: This function calls an API endpoint to fetch the latest conversion rate between two provided currencies. It takes three parameters: from_currency (the source currency code), to_currency (the target currency code), and amount (the amount in the source currency to be converted). It performs a check to see if the API call was successful, extracts the latest conversion rate and date from the response, and returns them as two separate objects. It returns None twice in case of an error.
    - `get_historical_rate(from_currency, to_currency, from_date, amount)`: This function calls an API endpoint to fetch the conversion rate between two provided currencies on a specific historical date. It takes four parameters: from_currency (the source currency code), to_currency (the target currency code), from_date (the historical date in the format "YYYY-MM-DD"), and amount (the amount in the source currency to be converted). It performs a check to see if the API call was successful, extracts the conversion rate from the response, and returns it. It returns None in case of an error.<br>
    These functions are used to interact with the Frankfurter API to retrieve currency conversion data, and the data is then processed and displayed in the Streamlit application in the code you provided.

3. **currency.py**:
    - `round_rate(rate)`:This function takes a floating-point number rate as input and rounds it to four decimal places.
    - `reverse_rate(rate)`: This function calculates the inverse of a given rate. If the rate is not equal to zero, it computes the reciprocal and rounds it to four decimal places. If the rate is zero, it returns 0.0000.
    - `format_output(date, from_currency, to_currency, rate, amount, converted_amount, inverse_rate)`: This function formats a text output containing conversion information and details. It takes several parameters: date (conversion date), from_currency (source currency code), to_currency (target currency code), rate (conversion rate), amount (original amount), converted_amount (amount after conversion), and inverse_rate (inverse conversion rate).

4. **frankfurter.py**:
    - `get_currencies_list()`: This function fetches a list of available currencies from the Frankfurter API. It sends a GET request to the API endpoint /currencies, retrieves the response, and parses it as JSON. If the HTTP status code is 200 (indicating a successful request), it returns a list of currency codes extracted from the JSON response. Otherwise, it returns None.
    - `get_latest_rates(from_currency, to_currency, amount)`: This function retrieves the latest exchange rate between two currencies. It takes three parameters: from_currency (source currency code), to_currency (target currency code), and amount (the amount in the source currency to convert). It constructs a URL with these parameters and sends a GET request to the API endpoint /latest. If the request is successful (status code 200), it extracts the date and the exchange rate from the JSON response and returns them as a tuple (date, rate). If the request fails, it returns two None values.
    - `get_historical_rate(from_currency, to_currency, from_date, amount)`: This function retrieves the historical exchange rate between two currencies on a specific date. It takes four parameters: from_currency (source currency code), to_currency (target currency code), from_date (the historical date in YYYY-MM-DD format), and amount (the amount in the source currency to convert). It constructs a URL with these parameters and sends a GET request to the API endpoint corresponding to the specified date. If the request is successful (status code 200), it extracts the exchange rate from the JSON response and returns it. If the request fails, it returns None.
    <br><br>
    These functions are responsible for fetching currency-related data from the Frankfurter API and handling the API responses and errors appropriately.