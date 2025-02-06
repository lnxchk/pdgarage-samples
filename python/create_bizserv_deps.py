"""
Service Relationships

Create a dependency between two services

https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE5Mg-associate-service-dependencies
"""
import os
import requests
import json

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# the "from" address has to be valid for a user in your account
from_address = os.environ['PD_FROM_ADDR']

supporting_service = input("Enter the ID of the supporting service: ")
dependent_service = input("Enter the ID of the dependent service: ")

data = {
    "relationships": [
        {
            "supporting_service": {
                "id": supporting_service,
                "type": "business_service"
            },
            "dependent_service": {
                "id": dependent_service,
                "type": "business_service"
            }
        }
    ]}

j_data = json.dumps(data)

print(j_data)

headers = {"Accept": "application/vnd.pagerduty+json;version=2",
           "Authorization": "Token token={}".format(api_token),
           "Content-Type": "application/json"}

url = 'https://api.pagerduty.com/service_dependencies/associate'
my_services = requests.post(url, headers=headers, data=j_data)
my_services.raise_for_status()

print(my_services.text)

