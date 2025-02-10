#!/usr/bin/env python3
"""
Create maintenance windows

Required info:
 * service ID
 * maintenance window start time
 * maintenance window end time
"""
# docs: https://developer.pagerduty.com/api-reference/a450bc9b9ea6f-create-a-maintenance-window
import os
import requests
import json

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# the "from" address has to be valid for a user in your account
from_address = os.environ['PD_FROM_ADDR']

maint_service = input("Enter the service ID for the maintenance window: ")
start_day = input("Enter the window start day YYYY-MM-DD: ")
start_time = input("Enter the window start time US/Eastern time HH:MM : ")
end_day = input("Enter the window end day: ")
end_time = input("Enter the window end time HH:MM : ")
description = input("Enter a description or contact person: ")

start_string = start_day + "T" + start_time + ":00-04:00"
end_string = end_day +"T" + end_time + ":00-04:00"
print("Setting maintenance window for {} to {}".format(start_string, end_string))

data = {
  "maintenance_window": {
    "type": "maintenance_window",
    "start_time": start_string,
    "end_time": end_string,
    "description": description,
    "services": [
      {
        "id": maint_service,
        "type": "service_reference"
      }
    ]
  }
}

j_data = json.dumps(data)

print(j_data)

headers = {"Accept": "application/vnd.pagerduty+json;version=2",
           "Authorization": "Token token={}".format(api_token),
           "Content-Type": "application/json"}

url = "https://api.pagerduty.com/maintenance_windows"
my_windows = requests.post(url, headers=headers, data=j_data)
print(my_windows.text)