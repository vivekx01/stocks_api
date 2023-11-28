from redis import Redis
import json
redis = Redis(host='192.168.0.107', port=6379, db=0)

def get_redis(key):
    if (redis.exists(key)):
        data = redis.get(key)
        return json.loads(data)
    else:
        return {"error":"The data does not exist on redis!"}

def set_redis(key,value):
    value_json= json.dumps(value)
    redis.set(key,value_json)

def redis_exists(key):
    return redis.exists(key)

def setex_redis(key,ttl,value):
    value_json= json.dumps(value)
    redis.setex(key,ttl,value_json)

def nse_get(key:str):
    symbol = key.upper()
    if (redis.hexists('nse_stock_mapping',symbol)):
        data = redis.hget('nse_stock_mapping',symbol)
        return data.decode('utf-8')
    else:
        return {"error":"The data does not exist on redis!"}

def nasdaq_get(key:str):
    symbol = key.upper()
    if (redis.hexists('nasdaq_stock_mapping',symbol)):
        data = redis.hget('nasdaq_stock_mapping',symbol)
        return data.decode('utf-8')
    else:
        return {"error":"The data does not exist on redis!"}
