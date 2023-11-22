from fastapi import APIRouter
from services.prices import get_stock_price

router = APIRouter()

@router.get("/prices/{stock_name}/")
def read_endpoint(stock_name: str):
    return get_stock_price(stock_name)
