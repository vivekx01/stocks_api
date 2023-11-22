import yfinance as yf
from fastapi import HTTPException, Depends
import ntplib
from datetime import datetime
import pytz
import time

def get_market_status():
    try:
        #getting the current day and time from ntp server
        ntp_server = 'pool.ntp.org'
        client = ntplib.NTPClient()
        response = client.request(ntp_server, version=3)
        timestamp = response.tx_time
        utc_datetime = datetime.utcfromtimestamp(timestamp).replace(tzinfo=pytz.utc)
        ist_timezone = pytz.timezone('Asia/Kolkata')
        ist_datetime = utc_datetime.astimezone(ist_timezone)
        current_time = ist_datetime.strftime("%H:%M:%S")
        current_day = ist_datetime.strftime("%A")
    except:
        return {"error":"Oops! Something went wrong! Try again after a few moments"}
    
    if current_day in ['Saturday', 'Sunday'] or not ('09:00:00' <= current_time <= '16:00:00'):
        market_status = 'Closed'
    else:
        print("This block is running")
        symbol = 'RELIANCE.NS' 
        interval = '1m'
        data = yf.Ticker(symbol).history(period='1d', interval=interval)
        previous_minute_close = data['Close'].iloc[-1]
        time.sleep(5)
        for _ in range(2):             
            data = yf.Ticker(symbol).history(period='1d', interval=interval)
            current_minute_close = data['Close'].iloc[-1]
            if current_minute_close != previous_minute_close:
                return {
                    'time': current_time,
                    'day': current_day,
                    'market_status': "Open"
                }
            time.sleep(5)
            previous_minute_close = current_minute_close
        market_status = "Closed"
    result = {
        'time': current_time,
        'day': current_day,
        'market_status': market_status
    }

    return result



