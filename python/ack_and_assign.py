"""
"""

import json
import os
import requests
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

headers = {"Accept": "application/vnd.pagerduty+json;version=2",
           "Authorization": "Token token={}".format(api_token),
           "Content-Type": "application/json",
           "From": "mwalls@pagerduty.com"}

print()

# create an incident


endpoint = "https://api.pagerduty.com/incidents/Q2P0OU7QZHLD48"
# For custom change event integrations, print the code. This is stored in the platform as-is.
data = {
  "incident": {
    "type": "incident",
    "assignments": [{
        "assignee": {
            "id": "PC6K5C9",
            "type": "user_reference"
        }
    }]
  }
}
j_data = json.dumps(data)
response = requests.put(endpoint, headers=headers, data=j_data)

response.raise_for_status()
print(response.text)
#
# response_object = json.dumps(response, indent=2)
#print(response_object)
