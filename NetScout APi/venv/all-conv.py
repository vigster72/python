import requests
import time
from datetime import datetime, timedelta
starttime = datetime.now() - timedelta(minutes=5, seconds=10)
start_time = starttime.strftime('%Y-%m-%d %H:%M:%S')
endtime = datetime.now()
end_time = endtime.strftime('%Y-%m-%d %H:%M:%S')
dummy_file = "/home/netscout/Downloads/all-conv.xml"
user_name = 'jvigliotti'
user_pass = 'Bat#cave0920'
server_ip = '172.23.246.3'
server_port = '443'
#This will open xml file to write xml field data
file = open(dummy_file,"w") #Creates the Api import file
#xml request for writing file
L1 = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'+"\n"
l1 = '<GenericClientQuery>'+"\n"
l2 = '<NetworkObjectData>'+"\n"
l3 = '<NetworkParameter>APPLICATION</NetworkParameter>'+"\n"
l4 = '<SelectColumnList>'+"\n"
l5 = '<ClientColumn>bitRate</ClientColumn>'+"\n"
l6 = '<ClientColumn>destAddress</ClientColumn>'+"\n"
l7 = '<ClientColumn>networkServiceId</ClientColumn>'+"\n"
l8 = '<ClientColumn>bitRateIn</ClientColumn>'+"\n"
l9 = '<ClientColumn>srcAddress</ClientColumn>'+"\n"
l10 = '<ClientColumn>targetTime</ClientColumn>'+"\n"
l11 = '</SelectColumnList>'+"\n"
l12 = '</NetworkObjectData>'+"\n"
l13 = '<FlowFilterList>'+"\n"
l14 = '<FlowFilter appliedServiceType="nwtservice" serviceId="61499420" serviceType="nwtservice">'+"\n"
l15 = '<FilterList><networkServiceId>61499420</networkServiceId>'+"\n"
l16 = '</FilterList>'+"\n"
l17 = '</FlowFilter>'+"\n"
l18 = '</FlowFilterList>'+"\n"
l19 = '<TimeDef><startTime>'+start_time+'</startTime>'+"\n"
l20 = '<endTime>'+end_time+'</endTime>'+"\n"
l21 = '<resolution>FIVE_MINUTE</resolution>'+"\n"
l22 = '<params>'+"\n"
l23 = '<columnOrder>true</columnOrder>'+"\n"
l24 = '<stringConversion>true</stringConversion>'+"\n"
l25 = '</params>'+"\n"
l26 = '</GenericClientQuery>'+"\n"

#write lines to file
file.writelines(L1)
file.writelines(l1)
file.writelines(l2)
file.writelines(l3)
file.writelines(l4)
file.writelines(l5)
file.writelines(l6)
file.writelines(l7)
file.writelines(l8)
file.writelines(l9)
file.writelines(l10)
file.writelines(l11)
file.writelines(l12)
file.writelines(l13)
file.writelines(l14)
file.writelines(l15)
file.writelines(l16)
file.writelines(l17)
file.writelines(l18)
file.writelines(l19)
file.writelines(l20)
file.writelines(l21)
file.writelines(l22)
file.writelines(l23)
file.writelines(l24)
file.writelines(l25)
file.writelines(l26)
# Closing file
file.close()
headers = {
    'Content-Type': 'application/xml',
    'Accept': 'text/csv',
}

data = open(dummy_file)
response = requests.post('https://'+server_ip+'/dbonequerydata/query', headers=headers, data=data, verify=False, auth=('user_name', 'user_pass'))
# ensure we notice bad responses
#response.raise_for_status()
# ensure we notice bad responses
#print(response.text)