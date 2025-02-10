#!/usr/bin/env python3
"""

Get all of the currently oncall responders in an account

"""

import os
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

print()

endpoint = "/oncalls"
response = session.rget(endpoint)

# pull the escalation policy and the level 1 oncall
for entry in response:
   print("{}:  {}".format(entry["escalation_policy"]["summary"], entry["user"]["summary"]))
