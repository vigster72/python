import time
import os
from datetime import datetime, timedelta
import os
starttime = datetime.now() - timedelta(minutes=5)
endtime = datetime.now()
#os.system('./dvasihist "Mib2IFTableRaw" ip=172.23.246.18 ifn=3 starttime='+starttime.strftime("%Y-%m-%d_%H:%M:%S")+'endtime='+endtime.strftime("%Y-%m-%d_%H:%M:%S")+ 'file=test.csv')
os.system('./dvdbonehist "Mib2IFTableRaw" starttime='+starttime.strftime("%Y-%m-%d_%H:%M:%S")+'endtime='+endtime.strftime("%Y-%m-%d_%H:%M:%S")+ 'file=test.csv')
print(starttime.strftime("%Y-%m-%d_%H:%M:%S"))
print(endtime.strftime("%Y-%m-%d_%H:%M:%S"))ostcoost

