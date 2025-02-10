#!/usr/bin/python3
"""
Query open incidents and display notes and alerts meeting a specific requirement.

The example matches "searchbe01" in the incident title.

"""

import os
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

print()

# Step 1: retrieve all incidents - sharpen this query to reduce number of responses.
#  Examples: Limit to certain teams. Limit to certain services. Limit to certain states.
endpoint = "/incidents"
response = session.rget(endpoint)

for incident in response:
    if "searchbe01" in incident['title']:
        id = incident['id']
    else:
        continue 

    # Step 2: retrieve notes
    endpoint = "/incidents/{}/notes".format(id)
    response = session.rget(endpoint)

    # response_object = json.dumps(response, indent=2)
    # print(response_object)

    print("THE NOTES FOR INCIDENT {}:".format(id))

    for note in response:
        print(note['created_at'], note['content'])

    # Step 3: retrieve alerts
    endpoint = "/incidents/{}/alerts".format(id)
    response = session.rget(endpoint)

    print("ALERTS:")
    # response_object = json.dumps(response, indent=2)
    # print(response_object)
    for alert in response:
        print("[{}]({})".format(alert['id'],alert['html_url']))

    print("*********************")