#!/usr/bin/env python3
"""
Example send an event to the events API v2

"""

import os
import requests
import json

# Routing Key for the events endpoint
route_key = os.environ['PD_ROUTE_KEY']


url = "https://events.pagerduty.com/v2/enqueue"
headers = {"Content-Type": "application/json"}

data = {
    "payload": {
        "summary": "nginx is not running",
        "severity": "critical",
        "source": "nginx.example.com"
    },
    "routing_key": "{}".format(route_key),
    "event_action": "trigger"
}

j_data = json.dumps(data)

print(j_data)

response = requests.post(url, headers=headers, data=j_data)
response.raise_for_status()
print(response.text)
