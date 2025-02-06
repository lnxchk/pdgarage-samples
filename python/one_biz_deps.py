"""
Service Dependencies Audit

This script will query your PagerDuty account for all dependency relationships
on a single service.

The dependency relationships aren't currently supported in pagerduty.

"""

import sys
import os
import requests

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']


# you can pass the service ID on the command line or enter it at the prompt
if len(sys.argv) < 2:
    this_service = input("Which service? ")
else:
    this_service = str(sys.argv[1])

print()
# get the services in the account, include the integrations
# https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE5Ng-list-services
url = "https://api.pagerduty.com/service_dependencies/business_services/{}".format(this_service)
headers = {"Accept": "application/vnd.pagerduty+json;version=2",
           "Authorization": "Token token={}".format(api_token),
           "Content-Type": "application/json"}

my_service = requests.get(url, headers=headers)

print(my_service.text)

# basic output, report with each service followed by its integrations.
# For custom change event integrations, print the code. This is stored in the platform as-is.

#if not len(my_service['relationships']) == 0:
#    print("RELATIONSHIPS:")
#    for i in my_service['relationships']:
#        print("Relationship ID: ", i['id'])
#else:
#    print("\tNo Dependency Relationships")
