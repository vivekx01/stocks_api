from fastapi import FastAPI
from api.endpoints import dividends_enpoint,financials_endpoint,prices_endpoint,stock_splits_endpoint

app = FastAPI()

app.include_router(dividends_enpoint.router)
app.include_router(financials_endpoint.router)
app.include_router(prices_endpoint.router)
app.include_router(stock_splits_endpoint.router)

