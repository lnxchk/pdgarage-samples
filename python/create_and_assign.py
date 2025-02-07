#!/usr/bin/env python3
"""
Create and Assign

Create an incident on a specified service, and assign a specific responder.
Pass the service ID and the responder's user ID on the command line
"""

import json
import sys
import os
import requests
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']
from_addr = os.environ['PD_FROM_ADDR']

# initialize the session
session = RestApiV2Client(api_token)

headers = {"Accept": "application/vnd.pagerduty+json;version=2",
           "Authorization": "Token token={}".format(api_token),
           "Content-Type": "application/json",
           "From": from_addr}

print()

# get inputs
service = sys.argv[1]
responder = sys.argv[2]
# create an incident


endpoint = "https://api.pagerduty.com/incidents"
# For custom change event integrations, print the code. This is stored in the platform as-is.
data = {
  "incident": {
    "type": "incident",
    "title": "The server is on fire",
    "assignments": [{
        "assignee": {
            "id": responder,
            "type": "user_reference"
        }
    }],
    "service": {
      "id": service,
      "summary": "",
      "type": "service_reference",
      "self": "",
      "html_url": ""
    }
  }
}
j_data = json.dumps(data)
response = requests.post(endpoint, headers=headers, data=j_data)

response.raise_for_status()
print(response.text)