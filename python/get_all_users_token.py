#!/usr/bin/env python3
"""
Get the users in an account, using a user token vs a global API Key
"""

import os
import requests

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
# api_token = os.environ['PD_API_KEY']
api_token = os.environ['USER_TOKEN']


BaseURL = "https://api.pagerduty.com"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/vnd.pagerduty+json;version=2",
    "Authorization": "Token token={}".format(api_token)
}

print()

endpoint = f"{BaseURL}/users/"
response = requests.get(endpoint, headers=headers)
response.raise_for_status()
print(response.text)
