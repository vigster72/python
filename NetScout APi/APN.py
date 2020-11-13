import json
import requests
api_header = {'Content-Type': 'application/json',}
api_APN_input = '{"apns": [{"addresses": ["bmc5.com"],"name": "BMC 5","dteSpeedKbps": 1000,"dceSpeedKbps": 1000}]}'
#
response = requests.post('https://192.168.87.62:8443/ng1api/ncm/apns',data=api_APN_input, auth=('administrator','netscout1'),verify=False,headers=api_header)
# ensure we notice bad responses
response.raise_for_status()
# ensure we notice bad responses
print(response.text)
