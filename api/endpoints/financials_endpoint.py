from fastapi import APIRouter
from services.financials import get_financials

router = APIRouter()

@router.get("/financials/{stock_name}/")
def read_endpoint(stock_name: str):
    return get_financials(stock_name)
