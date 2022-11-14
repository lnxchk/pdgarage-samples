"""
"""

import os
import json
from pdpyras import APISession
import requests
from datetime import datetime, timedelta, timezone

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = APISession(api_token)

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

endpoint = "{}/schedules/P05PEP7/overrides?since={}&until={}".format(BaseURL, since_time, until_time)
# print(endpoint)
querystring = {"since": since_time, "until": until_time}
response = requests.get(endpoint, headers=headers, params=querystring)
# response = session.rget(endpoint)
print(response.text)
# response_object = json.dumps(response.text, indent=2)
# print(response_object)

# walk the response array to get overrides for each schedule
# sched_id = response['id']
# sched_name = response['summary']
# oncall_user = response['users'][0]['summary']
#
# print("{} is oncall for schedule {}".format(oncall_user, sched_name))
