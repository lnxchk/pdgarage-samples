#!/usr/local/bin/python3
"""
"""

import sys
import os
import json
from datetime import datetime, timedelta, timezone
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

now_time = datetime.now(timezone.utc)
later_time = now_time + timedelta(28)
created_at_start = now_time.strftime("%Y-%m-%dT%H:%M:%S%z")
created_at_end = later_time.strftime("%Y-%m-%dT%H:%M:%S%z")
endpoint = "/schedules/{}".format(this_sched)
# basic output, report with each service followed by its integrations.
# For custom change event integrations, print the code. This is stored in the platform as-is.
response = session.rget(endpoint, params={'since':created_at_start, 'until':created_at_end})

# print(response)
response_object = json.dumps(response, indent=2)
print(response_object)
# formatted_response = json.loads(response_object)
# print(formatted_response)
