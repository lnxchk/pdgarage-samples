"""
Custom Change Event Transforms Integrations Audit

This script will query your PagerDuty account for one service. Add
that service to the URL on the "my_services =" line below.
 
If a service has an integration configured, show the id, summary, and 
code to run for that change event transform.

For more on integrations, see the Knowledge Base at
https://support.pagerduty.com/docs/services-and-integrations

For more on Change Event Transforms, see the Developer documentation at
https://developer.pagerduty.com/docs/ZG9jOjExMDI5NTgz-custom-change-event-transformer
"""

import os
from pdpyras import APISession


# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# the "from" address has to be valid for a user in your account
from_address = os.environ['PD_FROM_ADDR']

session = APISession(api_token, default_from=from_address)

# get the services in the account, include the integrations
# https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE5Ng-list-services
my_services = session.rget('/services/PSERVID', params={'include[]': 'integrations'})

# basic output, report with each service followed by its integrations.
# should be easy enough to change to csv or other formats if needed

#print(my_services)

print(my_services['id'])
print(my_services['name'])
for i in my_services['integrations']:
  print(i['id'])
  print(i['summary'])
  print(i['config']['fields']['code']['value'])

