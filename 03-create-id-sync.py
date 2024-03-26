#Create ID Sync

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

    "identitySync": {
      "syncName": "Demo",
      "configurations": {
        "activeDirectories": [
          {
            "name": "STARK_AD",
            "domain": "STARK.LOCAL",
            "directoryID": "f2c4a590-d0f6-11ee-9fe9-4ed55d83a1a6"
          }
        ]
      },
      "adGroups": [
        {
          "name": "stark.local/Users/Domain Admins",
          "sid": "S-1-5-21-3307156740-3824078416-2152747304-512",
          "source": "STARK_AD"
        }
      ],
      "syncSchedule": None
    }
  }
)


url = f"https://{ise1}:443/api/v1/duo-identitysync/identitysync"
response = requests.request("POST", url, auth=(un, pw), headers=headers, data=payload, verify=False)
print(response)
print(response.text)