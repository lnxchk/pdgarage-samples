#!/usr/bin/env python3
"""
Fetch the custom fields on a specific incident.

Include the incident ID on the command line or enter it at the prompt.

"""

import os
import sys
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

# you can pass the service ID on the command line or enter it at the prompt
if len(sys.argv) < 2:
    incident = input("Which incident? ")
else:
    incident = str(sys.argv[1])

print()

endpoint = f"https://api.pagerduty.com/incidents/{incident}/custom_fields/values"
response = session.get(endpoint)
print(response.text)
