#!/usr/local/bin/python3
"""
some scripts for accessing user info via the API
"""

import sys
import os
import json
from pdpyras import APISession

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = APISession(api_token)

endpoint = "/schedules"
# basic output, report with each service followed by its integrations.
# For custom change event integrations, print the code. This is stored in the platform as-is.
response = session.rget(endpoint)

# print(response)
for sched in response:
    # walk each schedule for a deleted user:
    # print(sched['id'])
    endpoint = "/schedules/{}/users".format(sched['id'])
    sched_users = session.rget(endpoint)
    for user in sched_users:
        if "deleted_at" in user:
            print(user['id'], user['summary'], " was deleted from ", sched['summary'])
