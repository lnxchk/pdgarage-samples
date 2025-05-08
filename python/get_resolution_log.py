#!/usr/bin/python3
"""
retrieve the resolution note from the log entries

"""

import os
import json
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

print()

# Step 1: retrieve all incidents - sharpen this query to reduce number of responses.
#  Examples: Limit to certain teams. Limit to certain services. Limit to certain states.
#  Paginate on your own
endpoint = "/log_entries"
response = session.rget(endpoint)

# response_object = json.dumps(response, indent=2)
# print(response_object)

for log_entry in response:
    if ("type" in log_entry['channel']) and (log_entry['channel']['type'] == "note"):
        if(log_entry['channel']['summary'].startswith("Resolution Note:")):
            print(log_entry['channel']['summary'])
        print("********")
        # if(log_entry['channel']['summary'].startswith("Resolution Note:")):
        #    print(log_entry)
#
#    if log_entry['channel']['type'].startswith("note") and log_entry['channel']['summary'].startswith("Resolution Note"):
#        print(log_entry['created_at'], log_entry['channel']['summary'])
