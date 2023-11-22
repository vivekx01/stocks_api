from fastapi import APIRouter
from services.dividends import latest_dividend_data

router = APIRouter()

@router.get("/dividends/{stock_name}/")
def read_endpoint(stock_name: str):
    return latest_dividend_data(stock_name)
