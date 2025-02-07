#!/usr/bin/env python3
"""
Analytics Query
Use the analytics endpoints to retrieve raw incident data 
based on a requested team.

See more about the analytics endpoints at
https://developer.pagerduty.com/
"""
import os
import sys
# import datetime, need timezone for Python 3.12+
from datetime import datetime, timedelta, timezone
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
# if using a user-level key, data will be limited by user 
# permissions. To use OAuth tokens, see the pagerduty docs
# https://pagerduty.github.io/pagerduty/user_guide.html#authentication
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

# you can pass the team ID on the command line or enter it at the prompt
if len(sys.argv) < 2:
    this_team = input("Which team? ")
else:
    this_team = str(sys.argv[1])

# print()

endpoint = "analytics/raw/incidents"
urgency = "high"
# statuses = ['resolved']
include = "teams"
team_ids = [this_team]
until_time = datetime.now(timezone.utc)
since_time = until_time - timedelta(14)
created_at_start = since_time.strftime("%Y-%m-%dT%H:%M:%S%z")
created_at_end = until_time.strftime("%Y-%m-%dT%H:%M:%S%z")

json_data = {
    "filters": {
        "urgency": urgency,
        "created_at_end": created_at_end,
        "team_ids": team_ids
    }
} 

# build the request with the JSON filter
resolved_incidents = session.rpost(
    endpoint,
    json=json_data
)

print(resolved_incidents)
for incident in resolved_incidents['data']:
    print("{},{},{}".format(incident['id'], incident['incident_number'], incident['description'] ))
