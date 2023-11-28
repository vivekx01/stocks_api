from celery import Celery
from utilities.redis_connect import set_redis,nasdaq_get,nse_get
from services.percent_change import minute_stock_price,hourly_stock_price,weekly_stock_price,daily_stock_price

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
        result.update({stock:get_price(stock,"nse")})
    set_redis('nifty_data',result)

@app.task
def get_nasdaq_data():
    stocks = [
        "ABNB", "ALGN", "AMD", "CEG", "AMZN", "AMGN", "AEP", "ADI", "ANSS", "AAPL",
        "AMAT", "GEHC", "ASML", "TEAM", "ADSK", "ADP", "AZN", "BKR", "AVGO", "BIIB",
        "BKNG", "CDNS", "ADBE", "CHTR", "CPRT", "CSGP", "CRWD", "CTAS", "CSCO", "CMCSA",
        "COST", "CSX", "CTSH", "DDOG", "DXCM", "FANG", "DLTR", "EA", "EBAY", "ENPH",
        "ON", "EXC", "FAST", "GFS", "META", "FI", "FTNT", "GILD", "GOOG", "GOOGL",
        "HON", "ILMN", "INTC", "INTU", "ISRG", "MRVL", "IDXX", "JD", "KDP", "KLAC",
        "KHC", "LRCX", "LCID", "LULU", "MELI", "MAR", "MCHP", "MDLZ", "MRNA", "MNST",
        "MSFT", "MU", "NFLX", "NVDA", "NXPI", "ODFL", "ORLY", "PCAR", "PANW", "PAYX",
        "PDD", "PYPL", "PEP", "QCOM", "REGN", "ROST", "SIRI", "SGEN", "SBUX", "SNPS",
        "TSLA", "TXN", "TMUS", "VRSK", "VRTX", "WBA", "WBD", "WDAY", "XEL", "ZM", "ZS"
    ]
    result={}
    for stock in stocks:
        result.update({stock:get_price(stock,"nasdaq")})
    set_redis('nasdaq_hundred_data',result)

def get_price(stock_symbol,stock_exchange):
    if (stock_exchange=="nse"):
        stock_name = nse_get(stock_symbol)
        minute = minute_stock_price(stock_symbol+".ns")
        hourly_change = hourly_stock_price(stock_symbol+".ns")
        daily_change = daily_stock_price(stock_symbol+".ns")
        weekly_change = weekly_stock_price(stock_symbol+".ns")
    else:
        stock_name = nasdaq_get(stock_symbol)
        minute = minute_stock_price(stock_symbol)
        hourly_change = hourly_stock_price(stock_symbol)
        daily_change = daily_stock_price(stock_symbol)
        weekly_change = weekly_stock_price(stock_symbol)
    
    response = {
        "stock_name": stock_name,
        "stock_symbol": stock_symbol,
        "price": minute,
        "hourly_change": hourly_change,
        "daily_change": daily_change,
        "weekly_change": weekly_change
    }
    return response
