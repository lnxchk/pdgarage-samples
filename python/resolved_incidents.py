"""
some playing around with the incidents endpoint

you'll need a valid API token and from: address
"""

import os
import json
from datetime import datetime, timedelta
from pdpyras import APISession

# example using curl:
# --url 'https://api.pagerduty.com/incidents?date_range=all&urgencies%5B%5D=high&statuses%5B%5D=triggered&include%5B%5D=users&service_ids%5B%5D=.......' \
# --header 'Accept: application/vnd.pagerduty+json;version=2' \
# --header 'Authorization: Token token=.+..................' \
# --header 'Content-Type: application/json'

# set some example parameters to play with
endpoint = "/incidents"
urgencies = ['high']
statuses = ['resolved']
include = "users"
team_ids = ["XXXXXXX"]
until_time = datetime.utcnow().date()
since_time = until_time - timedelta(30)

api_token = os.environ['PD_API_KEY']
from_addr = os.environ['PD_FROM_ADDR']
session = APISession(api_token, default_from=from_addr)

# query the API for all current incidents on the specified service
resolved_incidents = session.list_all(
    'incidents',
    params={'team_ids[]': team_ids, 'statuses[]': statuses, 'since': since_time, 'until': until_time, 'urgencies[]': urgencies}
)

# print(resolved_incidents)
response_object = json.dumps(resolved_incidents, indent=2)
print(response_object)
