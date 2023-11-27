from celery import Celery
from services.percent_change import get_percent_change
from utilities.redis_connect import set_redis

app = Celery('tasks')

@app.task
def get_nifty_data():
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
    set_redis('nifty_data',result)
