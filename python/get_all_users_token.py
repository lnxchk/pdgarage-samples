"""
"""

import json
import sys
import os
import requests
# from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
# api_token = os.environ['PD_API_KEY']
api_token = os.environ['ABBY_TOKEN']

# initialize the session
# session = RestApiV2Client(api_token)

BaseURL = "https://api.pagerduty.com"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/vnd.pagerduty+json;version=2",
    "Authorization": "Token token={}".format(api_token)
}

# you can pass the service ID on the command line or enter it at the prompt
# if len(sys.argv) < 2:
#    this_user = input("Which user? ")
# else:
#    this_user = str(sys.argv[1])

print()

endpoint = f"{BaseURL}/users/me"
# print(endpoint)
# basic output, report with each service followed by its integrations.
# For custom change event integrations, print the code. This is stored in the platform as-is.
response = requests.get(endpoint, headers=headers)
response.raise_for_status()
print(response.text)
# response_object = json.dumps(response, indent=2)
# print(response_object)
