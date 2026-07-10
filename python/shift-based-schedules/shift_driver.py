"""
Drive some of the functions in custom_shifts.py

"""


import sys
import os
import requests
import json
import csv
from datetime import datetime, timedelta
from custom_shifts import shifts_from_csv

# setting up for the v3 endpoint
host = "https://api.pagerduty.com/v3/schedules"

# set up other required headers 
# will change this when the python library is updated
api_token = os.environ['PD_API_KEY']
from_addr = os.environ['PD_FROM_ADDR']
headers = {"Accept": "application/json",
           "Authorization": "Token token={}".format(api_token),
           "Content-Type": "application/json",
           }

# schedule ID
schedule_id = "P6***OH"
# create custom shifts from csv file
filename = "shifts.csv"

shift_data = shifts_from_csv(filename)

# make the API call
endpoint = f"{host}/{schedule_id}/custom_shifts"
response = requests.post(endpoint, headers=headers, json=shift_data)
print(response.text)
