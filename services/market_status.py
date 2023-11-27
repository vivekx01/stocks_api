import yfinance as yf
import time
from utilities.redis_connect import get_redis,set_redis,redis_exists
from utilities.get_time import get_ist_time,get_et_time

def get_nse_market_status():
    try:
       ist_time = get_ist_time()
       current_date = ist_time['current_date']
       current_day = ist_time['current_day']
       current_time = ist_time['current_time']
    except Exception as e:
        return {"error":"Could not fetch time from ntp server, try again in few seconds"}
 
    response = {
        'date': current_date,
        'time': current_time+" IST",
        'day': current_day,
        'market_status': 'Not known'
    }

    # Market is open only Monday to friday 9:15am to 3:30pm
    if current_day in ['Saturday', 'Sunday'] or not ('09:15:00' <= current_time <= '15:30:00'):
        response['market_status'] = 'Closed'
        return response
    else:
        if (redis_exists('nse_market_status')):
            market_status_data = get_redis('nse_market_status')
            date_value = market_status_data['date'] 
            if(current_date==date_value):
                response['market_status'] = market_status_data['market_status']
                return response
        # Or else do the processing to detect if the market is open or closed
        symbol = 'RELIANCE.NS' 
        interval = '1m'
        data = yf.Ticker(symbol).history(period='1d', interval=interval)
        previous_minute_close = data['Close'].iloc[-1]
        time.sleep(5)
        for _ in range(2):             
            data = yf.Ticker(symbol).history(period='1d', interval=interval)
            current_minute_close = data['Close'].iloc[-1]
            #if it is detected that the market is open
            if current_minute_close != previous_minute_close:
                response['market_status'] = "Open"
                set_redis('nse_market_status',response)
                return response
            time.sleep(5)
            previous_minute_close = current_minute_close
        response['market_status'] = "Closed"
        set_redis('nse_market_status',response)
    return response

def get_nasdaq_market_status():
    try:
        #getting the current day and time from ntp server
        et_time = get_et_time()
        current_date = et_time['current_date']
        current_day = et_time['current_day']
        current_time = et_time['current_time']
    except Exception as e:
        return {"error":"Could not fetch time from ntp server, try again in few seconds"}
    
    response = {
        'date': current_date,
        'time': current_time + " ET",
        'day': current_day,
        'market_status': 'Not known'
    }

    # Market is open only Monday to friday 9am to 4pm
    if current_day in ['Saturday', 'Sunday'] or not ('09:30:00' <= current_time <= '16:00:00'):
        response['market_status'] = 'Closed'
        return response
    else:
        if (redis_exists('nasdaq_market_status')):
            market_status_data = get_redis('nse_market_status')
            date_value = market_status_data['date'] 
            if(current_date==date_value):
                response['market_status'] = market_status_data['market_status']
                return response
        # Or else do the processing to detect if the market is open or closed
        symbol = 'AAPL' 
        interval = '1m'
        data = yf.Ticker(symbol).history(period='1d', interval=interval)
        previous_minute_close = data['Close'].iloc[-1]
        time.sleep(5)
        for _ in range(2):             
            data = yf.Ticker(symbol).history(period='1d', interval=interval)
            current_minute_close = data['Close'].iloc[-1]
            #if it is detected that the market is open
            if current_minute_close != previous_minute_close:
                response['market_status'] = "Open"
                set_redis('nasdaq_market_status',response)
                return response
            time.sleep(5)
            previous_minute_close = current_minute_close
        response['market_status'] = "Closed"
        set_redis('nasdaq_market_status',response)
    return response



