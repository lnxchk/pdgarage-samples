"""
Service Integrations Audit
with Custom Change Events Code

This script will query your PagerDuty account for all integrations
on a single service.

If the service has a custom change event transform integration,
print the code of that integration.

For more on integrations, see the Knowledge Base at
https://support.pagerduty.com/docs/services-and-integrations

For more on the custom change event transform capability,
https://developer.pagerduty.com/docs/ZG9jOjExMDI5NTgz-custom-change-event-transformer
"""

import sys
import os
from pdpyras import APISession

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = APISession(api_token)

# you can pass the service ID on the command line or enter it at the prompt
if len(sys.argv) < 2:
    this_service = input("Which service? ")
else:
    this_service = str(sys.argv[1])

print()
# get the services in the account, include the integrations
# https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE5Ng-list-services
my_service = session.rget('/services/{}'.format(this_service), params={'include[]': 'integrations'})

# basic output, report with each service followed by its integrations.
# For custom change event integrations, print the code. This is stored in the platform as-is.

print(my_service['name'])
print(my_service['id'])
if not len(my_service['integrations']) == 0:
    print("INTEGRATIONS:")
    for i in my_service['integrations']:
        print("Integration ID: ", i['id'])
        print("Integration Summary: ", i['summary'])
        print("Integration URL: ", i['html_url'])
        print("Integration Type: ", i['type'])
        if i['vendor'] and i['vendor']['id'] == "PQ64Q6M":
            print('=' * 20)
            print("Custom Integration Code:")
            print('=' * 10)
            print(i['config']['fields']['code']['value'])
        print('=' * 20)
else:
    print("\tNo Integrations")
