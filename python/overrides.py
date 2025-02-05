"""
"""

import os
import json
from pagerduty import RestApiV2Client
import requests
from datetime import datetime, timedelta, timezone

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

BaseURL = "https://api.pagerduty.com/"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/vnd.pagerduty+json;version=2",
    "Authorization": "Token token={}".format(api_token)
}
# until = datetime.now(timezone.utc)
# since = until - timedelta(minutes=1)
since = datetime.now(timezone.utc)
until = since + timedelta(minutes=1)
since_time = since.isoformat()
until_time = until.isoformat()

s_endpoint = "schedules/PJ3GLH7/overrides"
r_endpoint = "{}/{}".format(BaseURL, s_endpoint)

querystring = {"since": since_time, "until": until_time}
r_response = requests.get(r_endpoint, headers=headers, params=querystring)
print(r_response.text)
print("****")
x_endpoint = "{}?since={}&until={}".format(r_endpoint, since_time, until_time)
print(x_endpoint)
x_response = requests.get(x_endpoint, headers=headers)
print(x_response.text)
print("****")

s_response = session.rget(s_endpoint, params=querystring)
print(s_response)
# response_object = json.dumps(response.text, indent=2)
# print(response_object)

