import sys
import os
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

# you can pass the service ID on the command line or enter it at the prompt
#if len(sys.argv) < 2:
#    this_service = input("Which service? ")
#else:
#    this_service = str(sys.argv[1])

print()

statuses = ["triggered", "acknowledged"]
long_incidents = session.list_all('incidents', params={'statuses[]': statuses, 'include[]': 'first_trigger_log_entries'})

print(long_incidents)
