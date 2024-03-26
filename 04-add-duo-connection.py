#Add Duo Connection

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

  "mfa": {
    "accountConfigurations": {
      "adminApi": {
        "ikey": "DI2NL8TDQC5CCCALI8BX",
        "sKey": "SoE4tkKOaXkqCbJoNkc9Bpwiy9V6FkbHSRrjmqd4"
      },
      "apiHostName": "api-demodemo.duosecurity.com",

      "authenticationApi": {
        "ikey": "DIB4V4692BWLH3UFN5YS",
        "sKey": "mhucTuIKXjnA7AdYo4TnOPDkvtNlh1todLGmS4Xb"
      }
    },
    "connectionName": "DuoConnection",
    "description": "",
    "identitySync": "Demo",
    "type": "VPN,TACACS"
  }

})


url = f"https://{ise1}:443/api/v1/duo-mfa/mfa"
response = requests.request("POST", url, auth=(un, pw), headers=headers, data=payload, verify=False)
print(response)
print(response.text)
