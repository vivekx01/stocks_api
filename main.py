from fastapi import FastAPI
import yfinance as yf
import pandas as pd
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"This is Stocks API"}

@app.get("/getdata/{stock_name}/")
def read_item(stock_name: str,query_param: str =None):
    try:
        price = get_stock_price(stock_name)
        dividends = latest_dividend_data(stock_name)
        splits = stock_splits(stock_name)
        financials = get_financials(stock_name)
        print(financials.head())
    except:
        return {"error": "Oops! Something went wrong!"}

    return {
            "stock_name": stock_name,
            "stock_price":f"{price:.2f}",
            "dividend_data":dividends,
            "stock_splits" : splits,
            # "financials": financials
            }

#getting stock price
def get_stock_price(name):
    # Define the symbol and timeframe
    symbol = name  # Replace with the symbol of the stock you're interested in
    interval = '1m'  # 1 minute intervals
    # Use the Ticker object to get intraday data
    data = yf.Ticker(symbol).history(period='1d', interval=interval)

    # Get the close price for the most recent minute
    current_minute_close = data['Close'].iloc[-1]
    return current_minute_close

def latest_dividend_data(name):
    dividends_data = yf.Ticker(name).dividends
    current_year = pd.to_datetime('today').year
    latest_year_dividends = dividends_data[dividends_data.index.year == current_year]
    return latest_year_dividends

def stock_splits(name):
    stock_splits = yf.Ticker(name).splits
    return stock_splits

def get_financials(name):
    financials = yf.Ticker(name).financials
    return financials