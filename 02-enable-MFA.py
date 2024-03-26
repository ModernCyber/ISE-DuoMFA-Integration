#Enable MFA

import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                         
ise1 = '198.19.10.11'
un = 'admin'
pw = 'C1sco12345'

headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
}

payload = json.dumps({
        'mfa' : {
        "status" : True 
    }
})


url = f"https://{ise1}:443/api/v1/duo-mfa/enable"
response = requests.request("PUT", url, auth=(un, pw), headers=headers, data=payload, verify=False)
print(response)
print(response.text)