"""
Service Integrations Audit

This script will query your PagerDuty account for all services. 
If a service has an integration configured, show the id, summary, and 
url for that integration.

For more on integrations, see the Knowledge Base at
https://support.pagerduty.com/docs/services-and-integrations

"""

import os
from pdpyras import APISession


# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']
from_addr = os.environ['PD_FROM_ADDR']

# the "from" address has to be valid for a user in your account
session = APISession(api_token, default_from=from_addr)

# get the services in the account, inslude the integrations
# https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE5Ng-list-services
my_services = session.rget('/services', params={'include[]': 'integrations'})

# basic output, report with each service followed by its integrations.
# should be easy enough to change to csv or other formats if needed
for i in my_services:
    # print(i['id'])
    if not len(i['integrations']) == 0:
        # print(i['integrations'])
        print("Service: {} {}".format(i['id'], i['name']))
        for integration in i['integrations']:
            print("\tID: {}, {} {}".format(integration['id'], integration['summary'], integration['html_url']))

        print("*" * 20)
