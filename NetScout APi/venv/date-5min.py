import requests
import time
from datetime import datetime, timedelta
starttime = datetime.now() - timedelta(minutes=5, seconds=10)
endtime = datetime.now()
end_time = endtime.strftime('%Y-%m-%d %H:%M:%S')
print (endtime.strftime('%Y-%m-%d %H:%M:%S'))
print (starttime.strftime('%Y-%m-%d %H:%M:%S'))
