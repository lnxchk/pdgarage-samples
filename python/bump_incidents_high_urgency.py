#!/usr/bin/env python3
"""
Bump Incidents High Urgency

Bump all incidents on a given service to high urgency.

May be helpful for services using support hours or other configurations.
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

# initialize the session
session = RestApiV2Client(api_token, default_from=from_address)

# you can pass the service ID on the command line or enter it at the prompt
if len(sys.argv) < 2:
    this_service = input("Which service? ")
else:
    this_service = str(sys.argv[1])

endpoint = "/incidents?service_ids[]={}&statuses[]=triggered".format(this_service)
for incident in session.iter_all(endpoint):
    incident['urgency'] = "high"
    put_endpoint = "/incidents/{}".format(incident['id'])
    updated_incident = session.rput(put_endpoint, json=incident)
    print(updated_incident)
