#!/usr/bin/env python3
"""
Get a list of currently active maintenance windows

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

print()

# several filters available for this query. see the docs for more info
endpoint = "maintenance_windows?filter=ongoing"
response = session.rget(endpoint)

# print(response)
for mw in response:
    print(mw['id'])
