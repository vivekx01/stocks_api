from fastapi import APIRouter
from services.stock_splits import stock_splits

router = APIRouter()

@router.get("/stock_splits/{stock_name}/")
def read_endpoint(stock_name: str):
    return stock_splits(stock_name)
