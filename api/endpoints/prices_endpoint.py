from fastapi import APIRouter
from services.prices import get_price

router = APIRouter()

@router.get("/price/{stock_name}/")
def read_endpoint(stock_name: str):
    return get_price(stock_name)

# @router.get("/prices/hour/{stock_name}/")
# def read_endpoint(stock_name: str):
#     return get_price(stock_name)

# @router.get("/prices/day/{stock_name}/")
# def read_endpoint(stock_name: str):
#     return daily_stock_price(stock_name)

# @router.get("/prices/week/{stock_name}/")
# def read_endpoint(stock_name: str):
#     return weekly_stock_price(stock_name)