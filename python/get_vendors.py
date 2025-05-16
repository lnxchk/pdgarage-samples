#!/usr/bin/env python3
"""
use the /vendor endpoint with a query string

"""

import sys
import os
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

# uncomment to query a single service
# you can pass the service ID on the command line or enter it at the prompt
if len(sys.argv) < 2:
    this_query = input("Enter query string: ")
else:
    this_query = str(sys.argv[1])

print()

endpoint = f"vendors?query={this_query}"
response = session.rget(endpoint)

# print(response)

for vendor in response:
    print(vendor['name'])
