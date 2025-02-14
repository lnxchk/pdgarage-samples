#!/usr/bin/env python3
"""

Find any users on the account who are not assigned to any oncall responsibilities

This was a question in the forums.
"""

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
response = session.rget(endpoint)

# print(response)
# The /oncalls endpoint surfaces all on call entries for a user
for user in response:
    all_oncalls = session.rget("/oncalls?user_ids[]={}".format(user['id']))
    if not all_oncalls:
        print("user {} is not in any oncall schedule or escalation policy".format(user['name']))
