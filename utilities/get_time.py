import ntplib
from datetime import datetime
import pytz
ntp_server = 'time.windows.com'
client = ntplib.NTPClient()
def get_ist_time():
    #getting the current day and time from ntp server
    response = client.request(ntp_server, version=3)
    timestamp = response.tx_time
    utc_datetime = datetime.utcfromtimestamp(timestamp).replace(tzinfo=pytz.utc)
    ist_timezone = pytz.timezone('Asia/Kolkata')
    ist_datetime = utc_datetime.astimezone(ist_timezone)
    current_time = ist_datetime.strftime("%H:%M:%S")
    current_day = ist_datetime.strftime("%A")
    current_date = ist_datetime.strftime("%Y-%m-%d")
    return {"current_time": current_time, "current_day":current_day, "current_date":current_date}

def get_et_time():
    #getting the current day and time from ntp server
    response = client.request(ntp_server, version=3)
    timestamp = response.tx_time
    utc_datetime = datetime.utcfromtimestamp(timestamp).replace(tzinfo=pytz.utc)
    et_timezone = pytz.timezone('US/Eastern')  # Eastern Time Zone
    et_datetime = utc_datetime.astimezone(et_timezone)
    current_time = et_datetime.strftime("%H:%M:%S")
    current_day = et_datetime.strftime("%A")
    current_date = et_datetime.strftime("%Y-%m-%d")
    return {"current_time": current_time, "current_day": current_day, "current_date": current_date}
