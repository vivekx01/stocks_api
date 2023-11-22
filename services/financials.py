import yfinance as yf

def get_financials(name):
    financials_data = yf.Ticker(name).financials
    financials_json = {}
    for key, value in financials_data.items():
        financials_json[key] = value.astype(str).to_dict()
    return {"stock_name":name,"financials":financials_json}