#!/usr/bin/env python3
"""
some playing around with the incidents endpoint

you'll need a valid API token and from: address
"""

import os
import json
from datetime import datetime, timedelta
from pagerduty import RestApiV2Client

# set some example parameters to play with
endpoint = "/incidents"
urgencies = ['high']
statuses = ['triggered']
include = "users"
team_ids = ["XXXXXXX"]
until_time = datetime.utcnow().date()
since_time = until_time - timedelta(30)

api_token = os.environ['PD_API_KEY']
from_addr = os.environ['PD_FROM_ADDR']
session = RestApiV2Client(api_token, auth_type='oauth2', default_from=from_addr)

# query the API for all current incidents on the specified service
resolved_incidents = session.list_all(
    'incidents',
    params={'statuses[]': statuses}
)

# print(resolved_incidents)
response_object = json.dumps(resolved_incidents, indent=2)
print(response_object)
