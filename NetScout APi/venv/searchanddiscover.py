import requests
import time
from datetime import datetime, timedelta
starttime = datetime.now() - timedelta(minutes=5, seconds=10)
endtime = datetime.now()
end_time = endtime.strftime('%Y-%m-%d %H:%M:%S')
#print (endtime.strftime('%Y-%m-%d %H:%M:%S'))
#print (starttime.strftime('%Y-%m-%d %H:%M:%S'))
dummy_file = "/home/netscout/Downloads/example.xml"
user_name = 'jvigliotti'
user_pass = 'Bat#cave0920'
server_ip = '172.23.246.11'
server_port = '443'
file = open(dummy_file,"w") #Creates the Api import file
#with open(import_file , 'r') as file:  # This csv data import to with Api
#    reader = csv.reader(file,delimiter = ',',skipinitialspace=True)
    #This creating the xml for the data extract
l1 = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'+"\n"
l2 = '<GenericClientQuery>'+"\n"
l3 = '<NetworkObjectData>'+"\n"
l4 = '<NetworkParameter>APPLICATION</NetworkParameter>'+"\n"
l5 = '<SelectColumnList>'+"\n"
l6 = '<ClientColumn>appId</ClientColumn>'+"\n"
l7 = '<ClientColumn>targetTime</ClientColumn>'+"\n"
l8 = '<ClientColumn>srcAddress</ClientColumn>'+"\n"
l9 = '<ClientColumn>srcToDestOctets</ClientColumn>'+"\n"
l10 = '<ClientColumn>srcToDestPackets</ClientColumn>'+"\n"
l11 = '<ClientColumn>srcPort</ClientColumn>'+"\n"
l12 = '<ClientColumn>destAddress</ClientColumn>'+"\n"
l13 = '<ClientColumn>destToSrcOctets</ClientColumn>'+"\n"
l14 = '<ClientColumn>destToSrcPackets</ClientColumn>'+"\n"
l15 = '<ClientColumn>destPort</ClientColumn>'+"\n"
l16 = '</SelectColumnList>'+"\n"
l17 = '</NetworkObjectData>'+"\n"
l18 = '<FlowFilterList>'+"\n"
l19 = '<FlowFilter appliedServiceType="nwtservice" serviceId="61499420" serviceType="nwtservice">'+"\n"
l20 = '<FilterList>'+"\n"
l21 = '<networkServiceId>61499420</networkServiceId>'+"\n"
#write lines to file
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
# Closing file
file.close()

# Checking if the data is
# written to file or not
#file = open(dummy_file, 'r')
#print(file.read())
#file.close()
#curl call to nG1
headers = {
    'Content-Type': 'application/xml',
    'Accept': 'text/csv',
}

data = open(dummy_file)
response = requests.post('https://'+server_ip+'/dbonequerydata/query', headers=headers, data=data, verify=False, auth=('user_name', 'user_pass'))
