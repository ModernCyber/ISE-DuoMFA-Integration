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


payload = json.dumps(
    
{
"condition": {
    "conditionType": "ConditionAttributes",
    "isNegate": False,
    "dictionaryName": "DEVICE",
    "attributeName": "Device Type",
    "operator": "equals",
    "dictionaryValue": None,
    "attributeValue": "All Device Types#Router"
},
"description": "",
"isProxy": False,
"name": "BRRTR Device Admin Policy Set 1",
"rank": 0,
"serviceName": "Default Device Admin",
"state": "enabled"
})

url = f"https://{ise1}:443/api/v1/policy/device-admin/policy-set"
response = requests.request("POST", url, auth=(un, pw), headers=headers, data=payload, verify=False)
policyId = response.json()['response']['id']
print(response)
print(response.text)


#MFA Rule

payload = json.dumps({

    "rule": {
      "default": False,
      "name": "MFA Rule",
      "hitCounts": 0,
      "rank": 0,
      "state": "enabled",
      "condition": {
        "link": None,
        "conditionType": "ConditionAttributes",
        "isNegate": False,
        "dictionaryName": "DEVICE",
        "attributeName": "Device Type",
        "operator": "equals",
        "dictionaryValue": None,
        "attributeValue": "All Device Types#Router"
      }
    },
    "mfaConnectionName": "DuoConnection",
    "mfaFailAction": "REJECT", 
    "mfaResultAction": "ACCEPT",
    }
)

url = f"https://{ise1}:443/api/v1/policy/device-admin/policy-set/{policyId}/mfa"
response = requests.request("POST", url, auth=(un, pw), headers=headers, data=payload, verify=False)
print(response)
print(response.text)

#Authorization Rule

payload = json.dumps({
    
  "commands": ["Helpdesk_IOS_Cmds"],
  "profile": "Helpdesk_IOS_Priv15",
  "rule": {
    "condition": {
        "conditionType": "ConditionAttributes",
        "isNegate": False,
        "dictionaryName": "STARK_AD",
        "attributeName": "ExternalGroups",
        "operator": "equals",
        "dictionaryValue": None,
        "attributeValue": "stark.local/Users/Domain Admins"
    },
    "default": False,
    "name": "Helpdesk Users",
    "rank": 0,
    "state": "enabled"
    }
})

url = f"https://{ise1}:443/api/v1/policy/device-admin/policy-set/{policyId}/authorization"
response = requests.request("POST", url, auth=(un, pw), headers=headers, data=payload, verify=False)