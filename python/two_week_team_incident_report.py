"""
"""

import json
import os
import sys
# import datetime
from datetime import datetime, timedelta, timezone
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

# you can pass the service ID on the command line or enter it at the prompt
if len(sys.argv) < 2:
    this_team = input("Which team? ")
else:
    this_team = str(sys.argv[1])

# print()

endpoint = "/incidents"
urgencies = ['high']
# statuses = ['resolved']
include = "teams"
team_ids = [this_team]
until_time = datetime.now(timezone.utc)
since_time = until_time - timedelta(45)
# basic output, report with each service followed by its integrations.
# For custom change event integrations, print the code. This is stored in the platform as-is.
# response = session.rget(endpoint)
resolved_incidents = session.list_all(
    'incidents',
    params={'team_ids[]': team_ids, 'since': since_time, 'until': until_time, 'urgencies[]': urgencies}
)

for incident in resolved_incidents:
    print("{},{}".format(incident['summary'], incident['id']))

