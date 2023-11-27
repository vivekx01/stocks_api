from fastapi import APIRouter
from services.percent_change import get_percent_change
router = APIRouter()

@router.get("/nse/{stock_symbol}/percent_change/")
def get_stock_percent_change(stock_symbol:str):
    return get_percent_change(stock_symbol+".ns")

@router.get("/nasdaq/{stock_symbol}/percent_change/")
def get_stock_percent_change(stock_symbol:str):
    return get_percent_change(stock_symbol)