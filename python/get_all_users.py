#!/usr/bin/env python3
"""
Get the users on a PagerDuty account using a global API key

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

print()

endpoint = "/users"
print(endpoint)
response = session.rget(endpoint)

response_object = json.dumps(response, indent=2)
print(response_object)
