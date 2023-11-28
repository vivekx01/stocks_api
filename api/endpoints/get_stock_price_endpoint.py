from fastapi import APIRouter
from services.get_stock_price import get_stock_price

router = APIRouter()


@router.get("/nse/{stock_symbol}/price")
def get_nse_stock_price(stock_symbol:str):
    return get_stock_price(stock_symbol,"nse")

@router.get("/nasdaq/{stock_symbol}/price")
def get_nasdaq_stock_price(stock_symbol:str):
    return get_stock_price(stock_symbol,"nasdaq")