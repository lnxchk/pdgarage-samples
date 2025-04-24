#!/usr/bin/env python3
"""
Asked in the forums. How to retrieve aggregate stats from API
"""

import json
import os
import sys
import pagerduty
from datetime import datetime, timedelta, timezone, date

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = pagerduty.RestApiV2Client(api_token)

# Potential filters for this query
# Team ID or Service ID is required for user-level API keys or OAuth keys
  # "created_at_start": 
  # "created_at_end":
  # "service_ids": [""]
  # "urgency": "high"
  # "major": true
  # "min_acknowledgements": 0
  # "min_timeout_escalations": 0
  # "min_manual_escalations": 0
  # "escalation_policy_ids": [""]
  # "priority_ids": [""]
  # "priority_names": ["P1", "P2"]
  # "pd_advance_used": true
today = datetime.now(timezone.utc)
since_time = date(2024, 1, 1).strftime("%Y-%m-%dT%H:%M:%SZ")
until_time = date(2024, 1, 31).strftime("%Y-%m-%dT%H:%M:%SZ")
# since_time = (today - timedelta(days = 180)).strftime("%Y-%m-%dT%H:%M:%SZ")
# until_time = (today - timedelta(days = 90)).strftime("%Y-%m-%dT%H:%M:%SZ")
put_data = {
  "filters": {
    "created_at_start": "2024-06-01T00:00:00-07:00",
    "created_at_end": "2024-12-31T23:59:59-07:00"
  },
  "time_zone": "Etc/UTC"
}

print()

endpoint = "/analytics/metrics/incidents/services/all"
# basic output, report with each service followed by its integrations.
# For custom change event integrations, print the code. This is stored in the platform as-is.
try:
  response = session.rpost(endpoint, json=put_data)
  response_object = json.dumps(response, indent=2)
  print(response_object)
except pagerduty.HttpError as e:
  raise e