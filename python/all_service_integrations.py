"""
Service Integrations Audit

This script will query your PagerDuty account for all services.
If a service has an integration configured, show the id, summary, and
url for that integration. 

For more on integrations, see the Knowledge Base at
https://support.pagerduty.com/docs/services-and-integrations

"""

import os
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# set up the session
session = RestApiV2Client(api_token)

# get the services in the account, include the integrations
# https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE5Ng-list-services
my_services = session.rget('/services', params={'include[]': 'integrations'})

# basic output, report with each service followed by its integrations.
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
        
