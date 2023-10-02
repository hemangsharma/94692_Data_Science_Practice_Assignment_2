# Building Currency Converter in Python #
## Student Details ##
<h3>Name: Hemang Sharma <br>
Student ID: 24695785</h3>

### Project Details ###

<li>app.py: main Streamlit python script used for managing users’ inputs and displaying results</li>
<li>api.py: python script that will contain the code for making API calls</li>
<li>frankfurter.py: python script that will contain the functions used for calling relevant Frankfurter endpoints and extracting information.</li>
<li>currency.py: python script that will contain the function used for formatting the results to be displayed in the Streamlit app.</li>
<li>README.md: a markdown file containing listing of all Python functions and instructions for running the web app</li>

### Functions Used ###

1. **app.py**:
   - Input fields: Use Streamlit's `number_input`, `selectbox`, and `date_input` functions to get user input for the amount, source currency, target currency, and optionally, a date for historical rates.
   - Conversion logic: When the "Convert" button is pressed, the selected date is converted to a string.
   - API calls: Depending on whether the selected date matches the current date, it fetches either the latest exchange rates or historical rates from the frankfurter API.
   - Currency conversion: If the API response contains rates, it calculates the converted amount based on the conversion rates, displays the result, and the inverse rate.

2. **api.py**:
   - `fetch_currencies()`: Fetches a list of available currencies from the Frankfurter API.
   - `fetch_latest_rate(from_currency, to_currency)`: Fetches the latest exchange rate between two currencies.
   - `fetch_historical_rate(from_currency, to_currency, date)`: Fetches the exchange rate between two currencies on a specific historical date.

3. **currency.py**:
   - `format_conversion_text(date, from_currency, to_currency, rate, amount, converted_amount, inverse_rate)`: Formats the conversion result and additional information into HTML text. It includes a bold and centered display of the conversion amount and a description of the conversion rate.

4. **frankfurter.py**:
   - `fetch_currencies()`: Fetches a list of available currencies from the Frankfurter API.
   - `fetch_latest_rates()`: Fetches the latest exchange rates from the Frankfurter API.
   - `fetch_historical_rates(date)`: Fetches historical exchange rates for a specific date from the Frankfurter API. In the `if __name__ == "__main__":` block, it also demonstrates how to fetch and store currencies, latest rates, and historical rates in JSON files.


### How to run ###

In order to run this program, type `streamlit run app.py` in the terminal from the directory where app.py is saved 