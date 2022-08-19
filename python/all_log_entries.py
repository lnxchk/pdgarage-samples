"""
use sparingly. or, honestly, not at all.

"""
import os
from pdpyras import APISession


# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# the "from" address has to be valid for a user in your account
from_address = os.environ['PD_FROM_ADDR']

session = APISession(api_token, default_from=from_address)

# get the services in the account, include the integrations
# https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE5Ng-list-services
my_log = session.rget('/log_entries')

# basic output, report with each service followed by its integrations.
# should be easy enough to change to csv or other formats if needed

print(my_log)
