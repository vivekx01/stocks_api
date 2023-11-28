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
        l=response["dividend_data"]
        dictionary=series_to_dict(l)
        response.update({"dividend_data":dictionary})
        
        l=response["stock_splits"]
        dictionary=series_to_dict(l)
        response.update({"stock_splits":dictionary})
        
        copy=response["financials"]
        list=[]
        for i in response["financials"]:
            list.append(i)
            
        for i in list:

            old_key = i
            new_key = str(i)

            copy[new_key] = copy.pop(old_key)

        response.update({"financials":copy})
        setex_redis(stock_symbol+"_info",exp_time,response)
        return response

def series_to_dict(s):
    ind=s.index.tolist()
    val=s.values.tolist()
    
    dictionary={}
    for i in range(len(ind)):
        dictionary.update({str(ind[i]):val[i]})
    return dictionary

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


