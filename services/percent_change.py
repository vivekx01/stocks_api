import yfinance as yf
from utilities.redis_connect import redis_exists,set_redis,setex_redis,get_redis

def get_percent_change(stock_symbol):
    if (redis_exists(stock_symbol+"_percent_change")):
        return get_redis(stock_symbol+"_percent_change")
    else:
        minute = minute_stock_price(stock_symbol)
        hourly_change = hourly_stock_price(stock_symbol)
        daily_change = daily_stock_price(stock_symbol)
        weekly_change = weekly_stock_price(stock_symbol)
        response = {
            "stock_symbol": stock_symbol,
            "price": minute,
            "hourly_change": hourly_change,
            "daily_change": daily_change,
            "weekly_change": weekly_change
        }
        setex_redis(stock_symbol+"_percent_change",60,response)
        return response

def minute_stock_price(name):
    symbol = name 
    interval = '1m'
    data = yf.Ticker(symbol).history(period='1d', interval=interval)
    current_minute_close = data['Close'].iloc[-1]
    return f"{current_minute_close:.2f}"

def hourly_stock_price(name):
    symbol = name  
    interval = '1h'
    data = yf.Ticker(symbol).history(period='1mo', interval=interval)
    close1 = data['Close'].iloc[-1]
    close2 = data['Close'].iloc[-2]
    percent_change = ((close1 - close2) * 100)/close2
    return f"{percent_change:.2f}"

def daily_stock_price(name):
    symbol = name
    interval = '1d'  
    data = yf.Ticker(symbol).history(period='1mo', interval=interval)
    close1 = data['Close'].iloc[-1]
    close2 = data['Close'].iloc[-2]
    percent_change = ((close1 - close2) * 100)/close2
    return f"{percent_change:.2f}"

def weekly_stock_price(name):
    symbol = name
    interval = '1wk' 
    data = yf.Ticker(symbol).history(period='3mo', interval=interval)
    close1 = data['Close'].iloc[-1]
    close2 = data['Close'].iloc[-2]
    percent_change = ((close1 - close2) * 100)/close2
    return f"{percent_change:.2f}"