from fastapi import FastAPI
from api.endpoints import dividends_enpoint,financials_endpoint,prices_endpoint,stock_splits_endpoint,market_status_endpoint
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins, allow all methods, allow all headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dividends_enpoint.router)
app.include_router(financials_endpoint.router)
app.include_router(prices_endpoint.router)
app.include_router(stock_splits_endpoint.router)
app.include_router(market_status_endpoint.router)


