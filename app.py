import streamlit as st
import pandas as pd
from frankfurter import fetch_latest_rates, fetch_historical_rates, fetch_currencies
from currency import format_conversion_text
import matplotlib.pyplot as plt

# Create a Streamlit web app
st.title("Currency Converter")

# Input fields
amount = st.number_input("Enter the amount to be converted", min_value=0.01, step=0.01)
from_currency = st.selectbox("Select the source currency", fetch_currencies())
to_currency = st.selectbox("Select the target currency", fetch_currencies())

date_input = st.date_input("Select a date (for historical rates)", min_value=pd.to_datetime('1999-01-04'), max_value=pd.to_datetime('today'))

# Button to trigger conversion
if st.button("Convert"):
    selected_date = date_input.strftime("%Y-%m-%d")  # Convert selected date to string
    current_date = "2023-09-29"  # Replace with the current date or fetch it dynamically

    # Fetch latest rates or historical rates
    if selected_date == current_date:
        data = fetch_latest_rates(from_currency, to_currency)
    else:
        data = fetch_historical_rates(selected_date)
    
    if "rates" in data:
        # Fetch conversion rates for both source and target currencies
        from_rate = data["rates"].get(from_currency)
        to_rate = data["rates"].get(to_currency)
        
        if from_rate is not None and to_rate is not None:
            # Convert the amount from source to target currency
            converted_amount = amount * (to_rate / from_rate)
            inverse_rate = 1 / (to_rate / from_rate)

            conversion_text = format_conversion_text(selected_date, from_currency, to_currency, to_rate, amount, converted_amount, inverse_rate)
            st.write(conversion_text, unsafe_allow_html=True)
            
        else:
            st.write(f"Currency code not found in API response.")
    else:
        st.write("Error fetching data from the API.")
