#!/usr/bin/env python3
"""
Get an incident
Pass the incident ID on the command line or enter it at the prompt

Use the environment variables to supply the API Key.

"""
import os
import sys
import json
from pagerduty import RestApiV2Client


# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# the "from" address has to be valid for a user in your account
from_address = os.environ['PD_FROM_ADDR']

session = RestApiV2Client(api_token, default_from=from_address)

if len(sys.argv) < 2:
  my_incident = input("Incident to show: ")
else:
  my_incident = str(sys.argv[1])

my_log = session.rget('/incidents/{}'.format(my_incident))

response_object = json.dumps(my_log, indent=2)
print(response_object)
