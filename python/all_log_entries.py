#!/usr/bin/env python3
"""
All Log Entries

Request all log entries 
See docs at https://developer.pagerduty.com/api-reference/c661e065403b5-list-log-entries

"""
import os
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# the "from" address has to be valid for a user in your account
from_address = os.environ['PD_FROM_ADDR']

session = RestApiV2Client(api_token, default_from=from_address)
my_log = session.rget('/log_entries')
print(my_log)
