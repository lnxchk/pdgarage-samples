"""
"""

import sys
import os
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

# get the user list
endpoint = "/users"
# basic output, report with each service followed by its integrations.
# For custom change event integrations, print the code. This is stored in the platform as-is.
response = session.rget(endpoint)

# print(response)
for user in response:
    all_oncalls = session.rget("/oncalls?user_ids[]={}".format(user['id']))
    if not all_oncalls:
        print("user {} is not in any oncall schedule or escalation policy".format(user['name']))
