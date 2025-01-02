"""
"""

import json
import os
import sys
from pdpyras import APISession

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = APISession(api_token)

# you can pass the service ID on the command line or enter it at the prompt
# if len(sys.argv) < 2:
#     this_service = input("Which service? ")
# else:
#     this_service = str(sys.argv[1])

print("Getting Event Orchestrations on the account")

endpoint = "/event_orchestrations"
# basic output, report with each service followed by its integrations.
# For custom change event integrations, print the code. This is stored in the platform as-is.
response = session.rget(endpoint)

response_object = json.dumps(response, indent=2)
print(response_object)

id = response[0]['id']

print("Getting the Router for the Event Orchestration {0}".format(id))

endpoint = "/event_orchestrations/{}/router".format(id)
router_response = session.rget(endpoint)

router_object = json.dumps(router_response, indent=2)
print(router_object)

catch_all = router_response['catch_all']
rules_set = router_response['sets'][0]['rules']

new_rules = {}
i = 0
for rule in rules_set:
    # leave out the rule I want to delete. I am matching by the id here, but you could also 
    #  match on the expression, or on the service ID of the target service
    if rule['id'] == "c7f568f9":
        next
    else:
        new_rules[i] = rule
        i += 1

print(new_rules)
data = {
    "orchestration_path": {
        "sets": [
            {
                "id": "start",
                "rules": new_rules
            }
        ]
    }
}

print(data)
print("Write back the deleted rule")

endpoint = "/event_orchestrations/{}/router".format(id)
writeback_response = session.rput(endpoint, json=data)