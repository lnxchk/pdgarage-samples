#!/usr/bin/env python3
"""
we want to replace one user with another user.
for example, a user leaves and organization and will be
replaced in the on-call schedule by someone else
"""

import sys
import os
import json
from pdpyras import APISession

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']
from_addr = os.environ['PD_FROM_ADDR']
# initialize the session
session = APISession(api_token)

# you can pass the service ID on the command line or enter it at the prompt
# if len(sys.argv) < 2:
#     this_service = input("Which service? ")
# else:
#     this_service = str(sys.argv[1])
# TODO: make input vars
my_sched = "P05PEP7"
old_user = "P9EGVWN"    # "Mandi At Work" user
new_user = "PQ99GXF"    # "Ben Developer" user

# get the new_user's info from the platform
ep = "/users/{}".format(new_user)
resp = session.rget(ep)
r_o = json.dumps(resp, indent=2)
# print(r_o)

# create a user object to push into the schedule
user_data = {
    "id": new_user,
    "type": "user_reference",
    "summary": resp['name'],
    "self": resp['self'],
    "html_url": resp['html_url']
}
# print(user_data)
json_ud = json.dumps(user_data)
# print(user_data)
endpoint = "/schedules/{}".format(my_sched)
# basic output, report with each service followed by its integrations.
# For custom change event integrations, print the code. This is stored in the platform as-is.
response = session.rget(endpoint)
# response_object = json.dumps(response, indent=2)
# print(response_object)

# add the new user to the top-level "users" array
response['users'].append(user_data)
# substitute in the new user

# need to go into each layer of the schedule
for layer in response['schedule_layers']:
    for user in layer['users']:
        # print(user)
        if user['user']['id'] == old_user:
            user['user'] = user_data

response_object = json.dumps(response, indent=2)
print(response_object)

# write back the schedule with the changes
write_back = session.rput(endpoint, json=response)
print(write_back)
