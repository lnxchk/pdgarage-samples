#!/usr/bin/env python3
"""
Delete a specific rule from an event orchestration.

"""

import json
import os
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

print("Getting Event Orchestrations on the account")

endpoint = "/event_orchestrations"
response = session.rget(endpoint)

response_object = json.dumps(response, indent=2)
print(response_object)

# TODO: Add a loop here to get all of the EOs 
id = response[0]['id']

print("Getting the Router for the Event Orchestration {0}".format(id))

endpoint = "/event_orchestrations/{}/router".format(id)
router_response = session.rget(endpoint)

router_object = json.dumps(router_response, indent=2)
print(router_object)

catch_all = router_response['catch_all']
rules_set = router_response['sets'][0]['rules']
rules_object = json.dumps(rules_set, indent=2)
print(rules_object)

rule_to_delete = input("Enter the ID of the rule to remove: ")


new_rules = {}
i = 0
for rule in rules_set:
    # leave out the rule I want to delete. I am matching by the id here, but you could also 
    #  match on the expression, or on the service ID of the target service
    if rule['id'] == rule_to_delete:
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