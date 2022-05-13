#!/usr/bin/env python3
"""
Looking for how long a responder was working on an incident.
This example queries a specific incident, looks through the log entries for responders added
to the incident directly - not the original assigned responder.  These responders might be
added via a response play or manually by another responder.

It then makes a note of the time the responder joined the incident, and the time the
incident was resolved.  It prints out how long each responder spent working on the incident,
assuming all responders worked on the incident from the time they joined until the incident
was resolved.

It's a bit of a blunt instrument, but might be helpful in some cases where these
responders don't show up in analytics reports.

This script will query the log for one particular incident in your account.

Use the environment variables to supply the API Key.

See the docs for the incident logs here:
https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE0Nw-list-log-entries-for-an-incident
"""
import os
import sys
import json
from datetime import datetime
from pdpyras import APISession


# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# the "from" address has to be valid for a user in your account
from_address = os.environ['PD_FROM_ADDR']

session = APISession(api_token, default_from=from_address)

if len(sys.argv) < 2:
  my_incident = input("Incident to show log entries for: ")
else:
  my_incident = str(sys.argv[1])

# get the services in the account, include the integrations
# https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE5Ng-list-services
my_log = session.rget('/incidents/{}/log_entries?is_overview=false'.format(my_incident), params={'include[]': 'channels'})

# basic output, report with each service followed by its integrations.
# should be easy enough to change to csv or other formats if needed

# if you want to see the complete objects, uncomment here
# print(my_log)
# response_object = json.dumps(my_log, indent=2)
# print(response_object)

responders = {}
resolve_time = ""

for i in my_log:
    #    print(i['summary'], "|",  i['created_at'])
    if "Joined" in i['summary']:
        responders[i['agent']['summary']] = i['created_at']
    if i['type'] == "resolve_log_entry":
        resolve_time = i['created_at']

# date format 2022-05-13T20:21:52Z
#             %Y-%m-%dT%H:%M:%SZ
res_time = datetime.strptime(resolve_time, "%Y-%m-%dT%H:%M:%SZ")
for resp in responders.keys():
    join_time = datetime.strptime(responders[resp], "%Y-%m-%dT%H:%M:%SZ")
    time_spent = res_time - join_time
    print(resp, "spent", time_spent, "on the incident")

# print(responders)
# print(resolve_time)



