from fastapi import APIRouter
from services.percent_change import minute_stock_price
from utilities.redis_connect import get_redis,setex_redis,redis_exists

router = APIRouter()

def get_stock_price(stock_symbol):
    if (redis_exists(stock_symbol+"_price")):
        return get_redis(stock_symbol+"_price")
    else:
        response = {"stock_symbol": stock_symbol, "stock_price": minute_stock_price(stock_symbol)}
        setex_redis(stock_symbol+"_price",1,response)
        return response
