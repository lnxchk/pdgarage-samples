#!/usr/bin/env python3
"""
Query the /escalation_policies/ endpoint for all EPs assigned to a specific team

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

# you can pass the team ID on the command line or enter it at the prompt
if len(sys.argv) < 2:
  this_team = input("Which team? ")
else:
  this_team = str(sys.argv[1])

print()

endpoint = "/escalation_policies?team_ids[]={}".format(this_team)

# to query for multiple teams, each team needs a team_ids[]=ID added

response = session.list_all(endpoint)
response_object = json.dumps(response, indent=2)
print(response_object)