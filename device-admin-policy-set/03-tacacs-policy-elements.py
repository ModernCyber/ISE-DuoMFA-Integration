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

# Command Set

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

#Profile

payload = json.dumps(
      {
      "TacacsProfile": {
          "name": "Helpdesk_IOS_Priv15",
          "description": "",
          "sessionAttributes": {
              "sessionAttributeList": [
                  {
                      "type": "MANDATORY",
                      "name": "priv-lvl",
                      "value": "1"
                  },
                  {
                      "type": "MANDATORY",
                      "name": "max_priv_lvl",
                      "value": "15"
                  }
              ]
          }
      }
    }  
  )

url = f"https://{ise1}:443/ers/config/tacacsprofile"
response = requests.request("POST", url, auth=(un, pw), headers=headers, data=payload, verify=False)
print(response)
print(response.text)
