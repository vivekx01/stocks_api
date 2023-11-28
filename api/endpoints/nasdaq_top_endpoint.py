from fastapi import APIRouter
from services.top_nasdaq import get_nasdaq_data 

router = APIRouter()


@router.get("/nasdaq/top-hundred/")
def get_top_nasdaq():
    response = get_nasdaq_data()
    return response
