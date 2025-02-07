#!/usr/local/bin/python3
"""
"""

# import sys
import os
import json
import requests
from datetime import datetime
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

# you can pass the service ID on the command line or enter it at the prompt
# if len(sys.argv) < 2:
#     this_service = input("Which service? ")
# else:
#     this_service = str(sys.argv[1])


month_beg = '2022-08-01T00:00:00Z'
month_end = '2022-08-31T23:59:59Z'
month_beg_time = datetime.strptime(month_beg, '%Y-%m-%dT%H:%M:%SZ')
month_end_time = datetime.strptime(month_end, '%Y-%m-%dT%H:%M:%SZ')

# print(month_beg_time, month_end_time)

s_id1 = "PCO0XEZ"
s_id2 = "PPBBGDI"

# endpoint = "/oncalls?since={}&until={}".format(month_beg_time, month_end_time)
# endpoint = "/oncalls"
# endpoint = "/oncalls?schedule_ids[]={}".format(s_id1)
# endpoint = "/oncalls?schedule_ids[]={}&schedule_ids[]={}".format(s_id1, s_id2)
endpoint = "/oncalls"

# basic output, report with each service followed by its integrations.
# For custom change event integrations, print the code. This is stored in the platform as-is.
response = session.rget(endpoint)

# print(response)

response_object = json.dumps(response, indent=2)
print(response_object)

# for ep in response:
#    print(ep['escalation_policy']['id'], ep['user']['summary'], ep['end'])	
