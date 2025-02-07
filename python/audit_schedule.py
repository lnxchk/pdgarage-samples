<<<<<<< HEAD
#!/usr/bin/env python3
"""
Audit Schedule

Show the record of changes that have been made to a schedule

=======
"""
>>>>>>> 68b2cb9e09cf23ea25b561a290b39628cf1aab5f
"""

import sys
import os
import json
import requests
# from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
# session = RestApiV2Client(api_token)

# you can pass the service ID on the command line or enter it at the prompt
if len(sys.argv) < 2:
    this_sched = input("Which schedule? ")
else:
    this_sched = str(sys.argv[1])

print()

endpoint = "/schedules/{}/audit/records".format(this_sched)
# basic output, report with each service followed by its integrations.
# For custom change event integrations, print the code. This is stored in the platform as-is.
# response = session.rget(endpoint)
headers = {"Accept": "application/vnd.pagerduty+json;version=2",
           "Authorization": "Token token={}".format(api_token),
           "Content-Type": "application/json"}
url = "https://api.pagerduty.com/schedules/{}/audit/records".format(this_sched)

response = requests.get(url, headers=headers)
print(response.text)

# response_object = json.dumps(response, indent=2)
# print(response_object)
# formatted_response = json.loads(response_object)
# print(formatted_response)
