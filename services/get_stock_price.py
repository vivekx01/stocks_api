from fastapi import APIRouter
from services.percent_change import minute_stock_price
from utilities.redis_connect import get_redis,setex_redis,redis_exists,nse_get,nasdaq_get

router = APIRouter()

def get_stock_price(stock_symbol,stock_exchange):
    if (redis_exists(stock_symbol+"_price")):
        return get_redis(stock_symbol+"_price")
    else:
        if (stock_exchange=="nse"):
            stock_name = nse_get(stock_symbol)
            stock_price = minute_stock_price(stock_symbol+".ns")
        else:
            stock_name = nasdaq_get(stock_symbol)
            stock_price= minute_stock_price(stock_symbol)
        response = {"stock_name":stock_name,"stock_symbol": stock_symbol, "stock_price": stock_price }
        setex_redis(stock_symbol+"_price",1,response)
        return response
