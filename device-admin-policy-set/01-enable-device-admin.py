#Enable Device Admin service

import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                         
ise1 = '198.19.10.11'
un = 'admin'
pw = 'C1sco12345'
hostname = 'ise1'

headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

payload = json.dumps({

    "hostname" : "ise1",
    "fqdn" : "ise1.stark.local",
    "ipAddress" : "198.19.10.11",
    "roles" : [ "Standalone" ],
    "services" : [ "Session", "Profiler", "pxGrid", "DeviceAdmin" ],
    "nodeStatus" : "Connected"

})


url = f"https://{ise1}:443/api/v1/deployment/node/{hostname}"
response = requests.request("PUT", url, auth=(un, pw), headers=headers, data=payload, verify=False)
print(response)
print(response.text)

