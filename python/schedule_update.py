"""
"""

import json
import os
import sys
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

# PGIRPOV

# you can pass the service ID on the command line or enter it at the prompt
if len(sys.argv) < 2:
    this_schedule = input("Which schedule? ")
else:
    this_schedule = str(sys.argv[1])

print(this_schedule)

endpoint = "/schedules/{}".format(this_schedule)
# basic output, report with each service followed by its integrations.
# For custom change event integrations, print the code. This is stored in the platform as-is.
response = session.rget(endpoint)

for user in response["schedule_layers"][0]["users"]:
    print("{} {}".format(user["user"]["summary"], user["user"]["id"]))

user1 = response["schedule_layers"][0]["users"][1]["user"]
user2 = response["schedule_layers"][0]["users"][2]["user"]

response["schedule_layers"][0]["users"][1]["user"] = user2
response["schedule_layers"][0]["users"][2]["user"] = user1

# print("User 1 is {}".format(user1["summary"]))
# print("User 2 is {}".format(user2["summary"]))

# check to ensure change was made in object
response_object = json.dumps(response, indent=2)
print(response_object)

# updated_response = session.put(endpoint, json=response)

# updated_response.raise_for_status()
# print(updated_response.text)
