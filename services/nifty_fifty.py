from services.percent_change import get_percent_change
from utilities.redis_connect import setex_redis,redis_exists,get_redis

def get_nifty_data():
    if (redis_exists('nifty_data')):
        return get_redis('nifty_data')
    else:
        stocks = ['CIPLA', 'DIVISLAB', 'ADANIENT', 'HINDALCO', 'JSWSTEEL', 'AXISBANK',
        'HDFCBANK', 'NTPC', 'ICICIBANK', 'M&M', 'DRREDDY', 'ASIANPAINT', 'HDFCLIFE',
        'MARUTI', 'LT', 'BAJAJ-AUTO', 'KOTAKBANK', 'SBIN', 'RELIANCE', 'ADANIPORTS',
        'BPCL', 'SBILIFE', 'BHARTIARTL', 'HINDUNILVR', 'LTIM', 'POWERGRID',
        'HEROMOTOCO', 'SUNPHARMA', 'BAJAJFINSV', 'GRASIM', 'TITAN', 'ITC', 'TATACONSUM',
        'ULTRACEMCO', 'INDUSINDBK', 'BAJFINANCE', 'COALINDIA', 'TECHM', 'EICHERMOT',
        'TATAMOTORS', 'TATASTEEL', 'NESTLEIND', 'ONGC', 'INFY', 'UPL', 'TCS',
        'BRITANNIA', 'WIPRO', 'HCLTECH', 'APOLLOHOSP']
        result={}
        for stock in stocks:
            result.update({stock:get_percent_change(stock+".ns")})
        setex_redis('nifty_data',30,result)
        return result

    