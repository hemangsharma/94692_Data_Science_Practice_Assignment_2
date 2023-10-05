import streamlit as st
import datetime
from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import format_output, reverse_rate

# Display Streamlit App Title
st.title("Currency Converter by Hemang")

# Add input fields for capturing amount, from and to currencies
amount = st.number_input("Enter the amount to be converted", min_value=0.01, step=0.01)
from_currency = st.selectbox("Select the source currency", get_currencies_list())
to_currency = st.selectbox("Select the target currency", get_currencies_list())

# Add a button to get and display the latest rate for selected currencies and amount
if st.button("Get Latest Rate"):
    latest_rates = get_latest_rates(from_currency, to_currency, amount)
    
    if latest_rates:
        date, rate = latest_rates  # Unpack the tuple
        converted_amount = amount * rate
        inverse_rate = reverse_rate(rate)
        output_text = format_output(date, from_currency, to_currency, rate, amount, converted_amount, inverse_rate)
        st.write(output_text)
    else:
        st.write("Error fetching latest rates.")

# Add a date selector (calendar)
selected_date = st.date_input("Select a date for historical rates", datetime.date.today(), datetime.date(1999, 1, 4))


# Add a button to get and display the historical rate for selected date, currencies, and amount
if st.button("Get Historical Rate"):
    historical_rate = get_historical_rate(from_currency, to_currency, selected_date, amount)
    
    if historical_rate:
        converted_amount = amount * historical_rate
        inverse_rate = reverse_rate(historical_rate)
        output_text = format_output(selected_date, from_currency, to_currency, historical_rate, amount, converted_amount, inverse_rate)
        st.write(output_text)
    else:
        st.write("Error fetching historical rate.")
