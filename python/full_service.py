#!/usr/bin/env python3
"""
Example service query with parameters and output parsing

"""

import os
import sys
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# the "from" address has to be valid for a user in your account
from_address = os.environ['PD_FROM_ADDR']

session = RestApiV2Client(api_token, default_from=from_address)

if len(sys.argv) < 2:
  service_id = input("Which service? ")
else:
  service_id = str(sys.argv[1])

# get the services in the account, include the integrations
# https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE5Ng-list-services
my_service = session.rget(f"/services/{service_id}", params={'include[]': 'integrations'})

print(my_service['id'])
print(my_service['name'])
for i in my_service['integrations']:
  print(i['id'])
  print(i['summary'])
  print(i['config']['fields']['code']['value'])

