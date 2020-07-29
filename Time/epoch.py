import time
from datetime import datetime, timedelta
starttime = datetime.now() - timedelta(minutes=5)
endtime = datetime.now().strftime('%s')
print (endtime)
print (starttime.strftime('%s'))