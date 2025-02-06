"""
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
# if len(sys.argv) < 2:
#     this_service = input("Which service? ")
# else:
#     this_service = str(sys.argv[1])

print()

endpoint = "/webhook_subscriptions"
# basic output, report with each service followed by its integrations.
# For custom change event integrations, print the code. This is stored in the platform as-is.
response = session.rget(endpoint)

# print(response)
# response_object = json.dumps(response, indent=2)
# print(response_object)
for resp in response:
    print(resp['description'])
    # print("\t", resp['filter']['id'])
    service = session.rget('/services/{}'.format(resp['filter']['id']))
    print("\t", service['summary'])

