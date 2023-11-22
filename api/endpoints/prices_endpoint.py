from fastapi import APIRouter
from services.prices import minute_stock_price,daily_stock_price,weekly_stock_price

router = APIRouter()

@router.get("/prices/minute/{stock_name}/")
def read_endpoint(stock_name: str):
    return minute_stock_price(stock_name)

@router.get("/prices/day/{stock_name}/")
def read_endpoint(stock_name: str):
    return daily_stock_price(stock_name)

@router.get("/prices/week/{stock_name}/")
def read_endpoint(stock_name: str):
    return weekly_stock_price(stock_name)