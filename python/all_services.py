"""
Service Integrations Audit
with Custom Change Event Transforms Code

This script will query your PagerDuty account for all services.
If a service has an integration configured, show the id, summary, and
url for that integration. If the integration is a Custom Change Event
Transform integration, print the code.

For more on integrations, see the Knowledge Base at
https://support.pagerduty.com/docs/services-and-integrations

For more on the custom change event transform capability,
https://developer.pagerduty.com/docs/ZG9jOjExMDI5NTgz-custom-change-event-transformer
"""

import os
from pdpyras import APISession

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# set up the session
session = APISession(api_token)

# get the services in the account, include the integrations
# https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE5Ng-list-services
my_services = session.rget('/services', params={'include[]': 'integrations'})

# basic output, report with each service followed by its integrations.
# for custom transforms, print the code. it is stored in the platform as-is.
for j in my_services:
    print('*=' * 10)
    print("Service ID:\t\t ", j['id'])
    print("Service Name:\t\t ", j['name'])
    print('*=' * 10)
    if not len(j['integrations']) == 0:
        print("INTEGRATIONS:")
        for i in j['integrations']:
            print("Integration Summary:\t ", i['summary'])
            print("Integration ID:\t\t ", i['id'])
            print("Integration URL:\t ", i['html_url'])
            print("Integration Type:\t ", i['type'])
            if i['vendor'] and i['vendor']['id'] == "PQ64Q6M":
                print('=' * 20)
                print("Custom Integration Code:")
                print('=' * 10)
                print(i['config']['fields']['code']['value'])
            print()
    else:
        print("\tNo Integrations")
        
