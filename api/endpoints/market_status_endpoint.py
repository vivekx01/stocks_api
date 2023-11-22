from fastapi import APIRouter
from services.market_status import get_market_status

router = APIRouter()

@router.get("/market_status")
def read_endpoint():
    return get_market_status()
