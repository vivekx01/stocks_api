from fastapi import APIRouter
from services.get_stock_info import stock_info

router = APIRouter()


@router.get("/nse/{stock_symbol}/info/")
def get_stock_info(stock_symbol:str):
    return stock_info(stock_symbol+".ns")

@router.get("/nasdaq/{stock_symbol}/info/")
def get_stock_info(stock_symbol:str):
    return stock_info(stock_symbol)