from fastapi import FastAPI
from api.endpoints import market_status_endpoint, get_stock_info_endpoint,get_stock_price_endpoint,percent_change_endpoint,nifty_fifty_endpoint,nasdaq_top_endpoint
from celery import Celery
from fastapi.middleware.cors import CORSMiddleware

celery = Celery(
    "tasks",
    broker="redis://192.168.0.107:6379/0",
    backend="redis://192.168.0.107:6379/0",
    include=["tasks"],
)

app = FastAPI()
celery.config_from_object('celery_config')

# Configure CORS
origins = [
    "http://localhost:4200",  # Add the origin of your Angular application
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can specify specific HTTP methods if needed
    allow_headers=["*"],  # You can specify specific HTTP headers if needed
)

app.include_router(market_status_endpoint.router)
app.include_router(get_stock_price_endpoint.router)
app.include_router(get_stock_info_endpoint.router)
app.include_router(percent_change_endpoint.router)
app.include_router(nifty_fifty_endpoint.router)
app.include_router(nasdaq_top_endpoint.router)
