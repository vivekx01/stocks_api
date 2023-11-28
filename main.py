from fastapi import FastAPI
from api.endpoints import market_status_endpoint, get_stock_info_endpoint,get_stock_price_endpoint,percent_change_endpoint,nifty_fifty_endpoint,nasdaq_top_endpoint
from celery import Celery

celery = Celery(
    "tasks",
    broker="redis://192.168.0.107:6379/0",
    backend="redis://192.168.0.107:6379/0",
    include=["tasks"],
)

app = FastAPI()
celery.config_from_object('celery_config')

app.include_router(market_status_endpoint.router)
app.include_router(get_stock_price_endpoint.router)
app.include_router(get_stock_info_endpoint.router)
app.include_router(percent_change_endpoint.router)
app.include_router(nifty_fifty_endpoint.router)
app.include_router(nasdaq_top_endpoint.router)
