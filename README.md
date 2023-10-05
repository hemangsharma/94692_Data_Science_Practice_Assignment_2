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
In order to run this program, type `streamlit run app.py` in the terminal from the directory where app.py is saved. For example `streamlit run /Users/hemang/Desktop/dsp_at2_24695785/app.py`

## Project Structure

The project consists of the following files:

1. app.py: The main Streamlit script for user input and displaying results.
2. api.py: Contains code for making API calls.
3. frankfurter.py: Includes functions for fetching exchange rate data from the Frankfurter API.
4. currency.py: Contains functions for formatting results to be displayed in the Streamlit app.
5. README.md: a markdown file containing listing of all Python functions and instructions for running the web app


