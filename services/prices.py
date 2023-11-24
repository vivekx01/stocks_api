import yfinance as yf


def minute_stock_price(name):
    # Define the symbol and timeframe
    symbol = name  # Replace with the symbol of the stock you're interested in
    interval = '1m'  # 1 minute intervals
    # Use the Ticker object to get intraday data
    data = yf.Ticker(symbol).history(period='1d', interval=interval)

    # Get the close price for the most recent minute
    current_minute_close = data['Close'].iloc[-1]
    return {"stock_name":name,"price":f"{current_minute_close:.2f}"}

def hourly_stock_price(name):
    # Define the symbol and timeframe
    symbol = name  # Replace with the symbol of the stock you're interested in
    interval = '1h'  # Daily intervals
    # Use the Ticker object to get daily data
    data = yf.Ticker(symbol).history(period='1mo', interval=interval)

    # Get the close price for the most recent day
    close1 = data['Close'].iloc[-1]
    close2 = data['Close'].iloc[-2]
    percent_change = ((close1 - close2) * 100)/close2
    return {"stock_name": name, "percent_change": f"{percent_change:.2f}"}

def daily_stock_price(name):
    # Define the symbol and timeframe
    symbol = name  # Replace with the symbol of the stock you're interested in
    interval = '1d'  # Daily intervals
    # Use the Ticker object to get daily data
    data = yf.Ticker(symbol).history(period='1mo', interval=interval)

    # Get the close price for the most recent day
    close1 = data['Close'].iloc[-1]
    close2 = data['Close'].iloc[-2]
    percent_change = ((close1 - close2) * 100)/close2
    return {"stock_name": name, "percent_change": f"{percent_change:.2f}"}

def weekly_stock_price(name):
    # Define the symbol and timeframe
    symbol = name  # Replace with the symbol of the stock you're interested in
    interval = '1wk'  # Weekly intervals
    # Use the Ticker object to get weekly data
    data = yf.Ticker(symbol).history(period='3mo', interval=interval)

    # Get the close price for the most recent week
    close1 = data['Close'].iloc[-1]
    close2 = data['Close'].iloc[-2]
    percent_change = ((close1 - close2) * 100)/close2
    return {"stock_name": name, "percent_change": f"{percent_change:.2f}"}