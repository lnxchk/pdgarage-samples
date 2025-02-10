#!/usr/bin/env python3
"""
  Acknowledge an incident
  Pass the incident ID on the command line

"""

import sys
import os
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']
from_addr = os.environ['PD_FROM_ADDR']

incident = sys.argv[1]

# initialize the session
session = RestApiV2Client(api_token, default_from=from_addr)

my_incident = session.rget(f"/incidents/{incident}")
my_incident['status'] = "acknowledged"
updated_incident = session.rput(f"/incidents/{incident}", json=my_incident)


