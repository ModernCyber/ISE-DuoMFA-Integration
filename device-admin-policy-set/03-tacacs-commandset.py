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
 # Helpdesk_IOS_Cmds Command Set

payload = json.dumps({
      
      "TacacsCommandSets": {
          "name": "Helpdesk_IOS_Cmds",
          "description": "",
          "permitUnmatched": False,
          "commands": {
              "commandList": [
                  {
                      "grant": "PERMIT",
                      "command": "ping",
                      "arguments": ""
                  },
                  {
                      "grant": "PERMIT",
                      "command": "show*",
                      "arguments": ""
                  }
              ]
          }
      }
  })

url = f"https://{ise1}:443/ers/config/tacacscommandsets"
response = requests.request("POST", url, auth=(un, pw), headers=headers, data=payload, verify=False)
print(response)
print(response.text)