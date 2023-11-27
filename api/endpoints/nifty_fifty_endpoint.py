from fastapi import APIRouter
from services.nifty_fifty import get_nifty_data

router = APIRouter()


@router.get("/nse/nifty-fifty/")
def get_nifty():
    return get_nifty_data