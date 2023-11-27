from fastapi import APIRouter
from services.market_status import get_nse_market_status,get_nasdaq_market_status

router = APIRouter()

@router.get("/nse/market_status")
def read_endpoint():
    return get_nse_market_status()

@router.get("/nasdaq/market_status")
def read_endpoint():
    return get_nasdaq_market_status()
