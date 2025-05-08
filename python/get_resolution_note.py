#!/usr/bin/python3
"""
retrieve the resolution note from incidents

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
#  Paginate on your own
endpoint = "/incidents"
response = session.rget(endpoint)

for incident in response:
    id = incident['id']

    # Step 1: retrieve notes
    endpoint = "/incidents/{}/notes".format(id)
    response = session.rget(endpoint)

    # response_object = json.dumps(response, indent=2)
    # print(response_object)

    print("THE NOTES FOR INCIDENT {}:".format(id))

    # Step 2: Find the Resolution Note
    for note in response:
        if note['content'].startswith("Resolution Note:"):
            print(note['created_at'], note['content'])

    print("*********************")