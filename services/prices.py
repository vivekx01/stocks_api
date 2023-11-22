import yfinance as yf
def get_stock_price(name):
    # Define the symbol and timeframe
    symbol = name  # Replace with the symbol of the stock you're interested in
    interval = '1m'  # 1 minute intervals
    # Use the Ticker object to get intraday data
    data = yf.Ticker(symbol).history(period='1d', interval=interval)

    # Get the close price for the most recent minute
    current_minute_close = data['Close'].iloc[-1]
    return {"stock_name":name,"price":f"{current_minute_close:.2f}"}