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
import requests
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

# you can pass the service ID on the command line or enter it at the prompt
if len(sys.argv) < 2:
    this_service = input("Which service? ")
else:
    this_service = str(sys.argv[1])

print()
# get the services in the account, include the integrations
# https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE5Ng-list-services
endpoint = "business_services/{}".format(this_service)
url = "https://api.pagerduty.com/{}".format(endpoint)
print(url)
headers = {"Accept": "application/vnd.pagerduty+json;version=2",
           "Authorization": "Token token={}".format(api_token),
           "Content-Type": "application/json"}
this_service_resp = requests.get(url, headers=headers)
service_obj = this_service_resp.json()
print(service_obj)
