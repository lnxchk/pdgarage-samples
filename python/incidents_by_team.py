#!/usr/bin/env python3
"""
https://community.pagerduty.com/forum/t/get-incident-count-by-team-for-particular-period/3827

Query the incidents endpoint to gather incident info for a specific team during a specific time frame.
"""

import sys
import os
import requests
from datetime import datetime, timedelta


# from pagerduty import RestApiV2Client


def GetIncidentCount(since, teamid):
    today = datetime.utcnow().date()
    querystring = {"since": since, "team_ids[]": teamid, "until": today}
    url = BaseURL + "incidents/count"
    count = requests.get(url, headers=headers, params=querystring).json()['total']
    return count


# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
# session = RestApiV2Client(api_token)
BaseURL = "https://api.pagerduty.com/"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/vnd.pagerduty+json;version=2",
    "Authorization": "Token token={}".format(api_token)
}

DateNow = datetime.utcnow().date()

# you can pass the team ID on the command line or enter it at the prompt
if len(sys.argv) < 2:
    my_team = input("Which team? ")
else:
    my_team = str(sys.argv[1])

print()

for n in range(30, 60):
    DateSince = datetime.utcnow().date() - timedelta(n)
    IncidentCount = GetIncidentCount(DateSince, my_team)
    ResultsRetStr = "{} days - {} incidents".format(n, IncidentCount)
    print(ResultsRetStr)

