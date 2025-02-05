"""
Some querying of the incident log

This script will query the log for one particular incident in your account.

Use the environment variables to supply the API Key.

See the docs for the incident logs here:
https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE0Nw-list-log-entries-for-an-incident
"""
import os
import sys
import json
from pagerduty import RestApiV2Client


# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# the "from" address has to be valid for a user in your account
from_address = os.environ['PD_FROM_ADDR']

session = RestApiV2Client(api_token, default_from=from_address)

if len(sys.argv) < 2:
  my_incident = input("Incident to show log entries for: ")
else:
  my_incident = str(sys.argv[1])

# get the services in the account, include the integrations
# https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE5Ng-list-services
my_log = session.rget('/incidents/{}'.format(my_incident))

# basic output, report with each service followed by its integrations.
# should be easy enough to change to csv or other formats if needed

# print(my_log)
response_object = json.dumps(my_log, indent=2)
print(response_object)

# for i in my_log['incidents_responders']:
#    print("User", i['user']['summary'], "added at", i['requested_at'], "status", i['state'], "at", i['updated_at'])
