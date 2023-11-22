import yfinance as yf

def stock_splits(name):
    stock_splits = yf.Ticker(name).splits
    return {"stock_name":name,"stock_splits":stock_splits}