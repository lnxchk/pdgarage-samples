#!/usr/bin/env python3
"""
Get info on a single user
Pass the user ID on the command line or enter it at the prompt
"""

import json
import sys
import os
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

# you can pass the service ID on the command line or enter it at the prompt
if len(sys.argv) < 2:
    this_user = input("Which user? ")
else:
    this_user = str(sys.argv[1])

print()

endpoint = f"/users/{this_user}"
print(endpoint)
response = session.rget(endpoint)

response_object = json.dumps(response, indent=2)
print(response_object)
