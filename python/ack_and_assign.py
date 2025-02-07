#!/usr/bin/env python3
"""
Ack and Assign
Acknowledge an incident and assign a responder

Command line args:
1. the incident ID
2. the user ID of the responder

"""

import json
import os
import sys
import requests

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']
from_addr = os.environ['PD_FROM_ADDR']

headers = {"Accept": "application/vnd.pagerduty+json;version=2",
           "Authorization": "Token token={}".format(api_token),
           "Content-Type": "application/json",
           "From": from_addr
           }


incident = sys.argv[1]
responder = sys.argv[2]

endpoint = "https://api.pagerduty.com/incidents/{}".format(incident)
# create the data structure to update the incident
data = {
  "incident": {
    "type": "incident",
    "assignments": [{
        "assignee": {
            "id": responder,
            "type": "user_reference"
        }
    }]
  }
}
j_data = json.dumps(data)
response = requests.put(endpoint, headers=headers, data=j_data)

response.raise_for_status()
print(response.text)