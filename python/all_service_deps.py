#!/usr/bin/env python3
"""
All Service Dependencies

Find the immediate service dependencies of a service.
Does not traverse the dependency tree.
Prompts for the service ID as input.

"""

import os
import requests
# from pagerduty import RestApiV2Client, HttpError

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

srv_input = input("Which service to query: ")

headers = {"Accept": "application/vnd.pagerduty+json;version=2",
           "Authorization": "Token token={}".format(api_token),
           "Content-Type": "application/json"}
url = 'https://api.pagerduty.com/'

try:
    url = 'https://api.pagerduty.com/service_dependencies/business_services/{}'.format(srv_input)
    my_services = requests.get(url, headers=headers)
    my_services.raise_for_status()
except requests.exceptions.RequestException:
    url = 'https://api.pagerduty.com/service_dependencies/technical_services/{}'.format(srv_input)
    print(url)
    my_services = requests.get(url, headers=headers)
except:
    print("Something else went wrong")

my_services = requests.get(url, headers=headers)
print(my_services.text)