from services.percent_change import get_percent_change
from utilities.redis_connect import setex_redis,redis_exists,get_redis

def get_nasdaq_data():
    if (redis_exists('nasdaq_hundred_data')):
        return get_redis('nasdaq_hundred_data')
    else:
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
        result=[]
        for stock in stocks:
            result.append(get_percent_change(stock))
        setex_redis('nasdaq_hundred_data',30,result)
        return result

    