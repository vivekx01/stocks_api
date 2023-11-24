import yfinance as yf
import ntplib
from datetime import datetime
import pytz
import time
import json

def get_market_status():
    try:
        #getting the current day and time from ntp server
        ntp_server = 'time.windows.com'
        client = ntplib.NTPClient()
        response = client.request(ntp_server, version=3)
        timestamp = response.tx_time
        utc_datetime = datetime.utcfromtimestamp(timestamp).replace(tzinfo=pytz.utc)
        ist_timezone = pytz.timezone('Asia/Kolkata')
        ist_datetime = utc_datetime.astimezone(ist_timezone)
        current_time = ist_datetime.strftime("%H:%M:%S")
        current_day = ist_datetime.strftime("%A")
        current_date = ist_datetime.strftime("%Y-%m-%d")

    except Exception as e:
        return {"error":"Oops! Something went wrong! Try again after a few moments"}
    
    # Market is open only Monday to friday 9am to 4pm
    if current_day in ['Saturday', 'Sunday'] or not ('09:15:00' <= current_time <= '15:30:00'):
        market_status = 'Closed'
    else:
        # Reading the stored json to get market status
        file_name = './services/market_status.json'
        with open(file_name, 'r') as file:
            market_status_data = json.load(file)
            date_value = market_status_data['date']
        # if there is already a stored value for the date
        if(current_date==date_value):
            return {
                    'date': current_date,
                    'time': current_time,
                    'day': current_day,
                    'market_status': market_status_data['market_status']
            }
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
                market_status_data['date']=current_date
                market_status_data['market_status']="Open"
                with open(file_name, 'w') as file:
                    # Write the modified JSON data to file
                    json.dump(market_status_data, file, indent=2)
                return {
                    'date': current_date,
                    'time': current_time,
                    'day': current_day,
                    'market_status': "Open"
                }
            time.sleep(5)
            previous_minute_close = current_minute_close
        market_status = "Closed"
    result = {
        'date': current_date,
        'time': current_time,
        'day': current_day,
        'market_status': market_status
    }

    return result



