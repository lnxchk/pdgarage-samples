"""
"""

# import sys
import os
import requests
import json
# from pagerduty import EventsAPIV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
# session = EventsAPIV2Client(api_token)

# you can pass the service ID on the command line or enter it at the prompt
# if len(sys.argv) < 2:
#     this_service = input("Which service? ")
# else:
#     this_service = str(sys.argv[1])

# basic output, report with each service followed by its integrations.
# For custom change event integrations, print the code. This is stored in the platform as-is.
url = "https://events.pagerduty.com/v2/enqueue"
headers = {"Content-Type": "application/json"}

data = {
    "payload": {
        "summary": "nginx is not running",
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
