import pandas as pd
import redis

def populate_redis(csv_file, redis_key, redis_conn):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Convert DataFrame to dictionary for efficient mapping
    mapping_dict = df.set_index('Symbol')['Name'].to_dict()

    # # Populate Redis database
    for Symbol, Name in mapping_dict.items():
        redis_conn.hset(redis_key, Symbol, Name)

if __name__ == "__main__":
    # Replace these values with your actual file paths and Redis connection details
    nse_csv_file = './csv/nse_list.csv'
    nasdaq_csv_file = './csv/nasdaq_list.csv'
    
    redis_host = '192.168.0.107'
    redis_port = 6379
    redis_db = 0
    redis_key_nse = 'nse_stock_mapping'
    redis_key_nasdaq = 'nasdaq_stock_mapping'

    # Connect to Redis
    redis_conn = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

    # Populate Redis for NSE stocks
    populate_redis(nse_csv_file, redis_key_nse, redis_conn)

    # Populate Redis for NASDAQ stocks
    populate_redis(nasdaq_csv_file, redis_key_nasdaq, redis_conn)

    print("Data populated to Redis successfully.")
