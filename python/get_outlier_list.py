"""
Determine if an incident is an anomaly via the API

Use the environment variables to supply the API Key.

"""
import os
import sys
import json
import pagerduty

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# the "from" address has to be valid for a user in your account
from_address = os.environ['PD_FROM_ADDR']

session = pagerduty.RestApiV2Client(api_token, default_from=from_address)

# Step 1: get a list of incidents
my_incidents = session.rget('/incidents')

for incident in my_incidents:
    id = incident['id']
    # Step: is the incident an anomaly? 
    # make a request for outlier_incident
    # if the incident DOES NOT HAVE an entry in the outliers, it returns a 404!
    # Outliers can be novel, frequent, and rare
    # see https://developer.pagerduty.com/api-reference/bc1ec9fb359f8-get-outlier-incident
    try: 
      is_outlier = session.rget('/incidents/{}/outlier_incident'.format(id))
    except pagerduty.HttpError as e:
       if e.response.status_code == 404:
          continue
          
    print("{} is {}".format(id, is_outlier['incident']['occurrence']['category']))
