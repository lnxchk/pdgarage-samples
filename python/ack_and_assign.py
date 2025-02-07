<<<<<<< HEAD
#!/usr/bin/env python3
"""
Ack and Assign
Acknowledge an incident and assign a responder

Command line args:
1. the incident ID
2. the user ID of the responder

=======
"""
>>>>>>> 68b2cb9e09cf23ea25b561a290b39628cf1aab5f
"""

import json
import os
<<<<<<< HEAD
import sys
import requests
=======
import requests
from pagerduty import RestApiV2Client
>>>>>>> 68b2cb9e09cf23ea25b561a290b39628cf1aab5f

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']
<<<<<<< HEAD
from_addr = os.environ['PD_FROM_ADDR']
=======

# initialize the session
session = RestApiV2Client(api_token)
>>>>>>> 68b2cb9e09cf23ea25b561a290b39628cf1aab5f

headers = {"Accept": "application/vnd.pagerduty+json;version=2",
           "Authorization": "Token token={}".format(api_token),
           "Content-Type": "application/json",
<<<<<<< HEAD
           "From": from_addr
           }


incident = sys.argv[1]
responder = sys.argv[2]

endpoint = "https://api.pagerduty.com/incidents/{}".format(incident)
# create the data structure to update the incident
=======
           "From": "mwalls@pagerduty.com"}

print()

# create an incident


endpoint = "https://api.pagerduty.com/incidents/Q2P0OU7QZHLD48"
# For custom change event integrations, print the code. This is stored in the platform as-is.
>>>>>>> 68b2cb9e09cf23ea25b561a290b39628cf1aab5f
data = {
  "incident": {
    "type": "incident",
    "assignments": [{
        "assignee": {
<<<<<<< HEAD
            "id": responder,
=======
            "id": "PC6K5C9",
>>>>>>> 68b2cb9e09cf23ea25b561a290b39628cf1aab5f
            "type": "user_reference"
        }
    }]
  }
}
j_data = json.dumps(data)
response = requests.put(endpoint, headers=headers, data=j_data)

response.raise_for_status()
<<<<<<< HEAD
print(response.text)
=======
print(response.text)
#
# response_object = json.dumps(response, indent=2)
#print(response_object)
>>>>>>> 68b2cb9e09cf23ea25b561a290b39628cf1aab5f
