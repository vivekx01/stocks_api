import yfinance as yf
import pandas as pd
from datetime import timedelta
from utilities.redis_connect import redis_exists,setex_redis,get_redis

def stock_info(stock_symbol):
    if (redis_exists(stock_symbol+"_info")):
        return get_redis(stock_symbol+"_info")
    else:
        response = {
            "dividend_data" : latest_dividend_data(stock_symbol),
            "stock_splits" : stock_splits(stock_symbol),
            "financials" : get_financials(stock_symbol)
        }
        exp_time = timedelta(days=90)
        # setex_redis(stock_symbol+"_info",exp_time,response)
        return response
    
def latest_dividend_data(name):
    dividends_data = yf.Ticker(name).dividends
    current_year = pd.to_datetime('today').year
    last_4_years = range(current_year - 3, current_year + 1)
    latest_4_years_dividends = dividends_data[dividends_data.index.year.isin(last_4_years)]
    return latest_4_years_dividends

def get_financials(name):
    financials_data = yf.Ticker(name).financials
    financials_json = {}
    for key, value in financials_data.items():
        financials_json[key] = value.astype(str).to_dict()
    return financials_json

def stock_splits(name):
    stock_splits = yf.Ticker(name).splits
    return stock_splits


