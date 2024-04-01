#Enable Device Admin service

import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                         
ise1 = '198.19.10.11'
un = 'admin'
pw = 'C1sco12345'

headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

payload = json.dumps({
    
    "NetworkDevice": {
    "name": "BRRTR",
    "authenticationSettings": {
      "networkProtocol": "RADIUS",
      "radiusSharedSecret": "C1sco12345",
      "enableKeyWrap": False,
      "dtlsRequired": False,
      "enableMultiSecret": False,
      "keyEncryptionKey": "",
      "messageAuthenticatorCodeKey": "",
      "keyInputFormat": "ASCII"
    },
    "tacacsSettings": {
    "sharedSecret": "C1sco12345",
    "connectModeOptions": "ON_LEGACY"
    },
    "profileName": "Cisco",
    "coaPort": 1700,
    "NetworkDeviceIPList": [
      {
        "ipaddress": "198.18.133.101",
        "mask": 32
      }
    ],
  }
})


url = f"https://{ise1}:443/ers/config/networkdevice"
response = requests.request("POST", url, auth=(un, pw), headers=headers, data=payload, verify=False)
print(response)
print(response.text)