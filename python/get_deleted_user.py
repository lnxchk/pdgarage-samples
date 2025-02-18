#!/usr/bin/env python3
"""
Query the /schedules/ endpoint looking for users deleted from schedules
"""

import os
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

endpoint = "/schedules"
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
