import yfinance as yf
import pandas as pd

def latest_dividend_data(name):
    dividends_data = yf.Ticker(name).dividends
    current_year = pd.to_datetime('today').year
    # Get the last 4 years from the current date
    current_year = pd.to_datetime('today').year
    last_4_years = range(current_year - 3, current_year + 1)

    # Filter dividends data for the last 4 years
    latest_4_years_dividends = dividends_data[dividends_data.index.year.isin(last_4_years)]

    return {"stock_name":name,"dividends":latest_4_years_dividends}