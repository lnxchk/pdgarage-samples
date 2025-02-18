#!/usr/bin/env python3
"""
Query the /incidents/ endpoint using all of the include[] parameters

"""

import os
import json
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

# print()

endpoint = "/incidents?include[]=users&include[]=services&include[]=first_trigger_log_entries&include[]=escalation_policies&include[]=teams&include[]=assignees&include[]=acknowledgers&include[]=priorities&include[]=conference_bridge"
response = session.rget(endpoint)

# print(response)
response_object = json.dumps(response, indent=2)
print(response_object)
