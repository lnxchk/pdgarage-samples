#!/usr/bin/env python3
"""
Get all responders included in a schedule

Pass the schedule ID on the command line or enter it at the prompt
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
    this_sched = input("Which schedule? ")
else:
    this_sched = str(sys.argv[1])

# option 1: get all the users on a schedule
endpoint = "/schedules/{}/users".format(this_sched)
response = session.rget(endpoint)

# option 2: use the /oncalls endpoint to find their shifts
# the info is similar but not exactly the same.
# endpoint = "/oncalls"
# response = session.rget(endpoint, params={'schedule_ids[]': this_sched})

# print(response)
response_object = json.dumps(response, indent=2)
print(response_object)
# formatted_response = json.loads(response_object)
# print(formatted_response)
