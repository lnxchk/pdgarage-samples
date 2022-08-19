
import os
import json
import requests
from pdpyras import APISession

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_ROUTE_KEY']

# initialize the session
session = APISession(api_token)

# basic output, report with each service followed by its integrations.
# For custom change event integrations, print the code. This is stored in the platform as-is.
url = "https://events.pagerduty.com/v2/enqueue"
headers = {"Content-Type": "application/json"}

data = {
    "payload": {
        "summary": "Service 'nginx' is DOWN",
        "severity": "critical",
        "source": "nginx.example.com"
    },
    "routing_key": "{}".format(api_token),
    "event_action": "trigger"
}

j_data = json.dumps(data)

print(j_data)

response = requests.post(url, headers=headers, data=j_data)
response.raise_for_status()
print(response.text)
