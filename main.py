from fastapi import FastAPI, BackgroundTasks, Depends
from api.endpoints import dividends_enpoint, financials_endpoint, prices_endpoint, stock_splits_endpoint, market_status_endpoint
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from redis import Redis

app = FastAPI()

# Allow all origins, allow all methods, allow all headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

redis = Redis(host='192.168.0.107', port=6379, db=0)

async def update_data_in_redis(background_tasks: BackgroundTasks):
    # Perform the update operation here (replace with your logic)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    redis.set("latest_data", f"Updated data at {current_time}")


@app.on_event("startup")
async def startup_event():
    # Start the background task when the FastAPI app starts
    background_tasks = BackgroundTasks()
    background_tasks.add_task(update_data_in_redis, background_tasks)
    # Pass the background_tasks object to the update_data_in_redis function
    await update_data_in_redis(background_tasks)

@app.get("/test_redis")
def get_latest_data():
    # Retrieve the latest data from Redis
    latest_data = redis.get("latest_data")
    if latest_data:
        return {"latest_data": latest_data.decode()}
    else:
        return {"message": "No data available"}

app.include_router(dividends_enpoint.router)
app.include_router(financials_endpoint.router)
app.include_router(prices_endpoint.router)
app.include_router(stock_splits_endpoint.router)
app.include_router(market_status_endpoint.router)
