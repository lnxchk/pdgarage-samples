#!/usr/bin/env python3
"""
Get a single escalation policy from the PagerDuty account

Pass the escalation policy ID on the command line or enter it at the prompt
"""

import sys
import os
import json
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

# you can pass the service ID on the command line or enter it at the prompt
if len(sys.argv) < 2:
  esc_pol = input("Which escalation policy? ")
else:
  esc_pol = str(sys.argv[1])

print()

# build request
endpoint = f"escalation_policies/{esc_pol}/"
response = session.rget(endpoint)

# print(response)
response_object = json.dumps(response, indent=2)
print(response_object)
