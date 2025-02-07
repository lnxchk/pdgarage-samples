<<<<<<< HEAD
#!/usr/bin/env python3
"""
All Log Entries

Request all log entries 
See docs at https://developer.pagerduty.com/api-reference/c661e065403b5-list-log-entries
=======
"""
use sparingly. or, honestly, not at all.
>>>>>>> 68b2cb9e09cf23ea25b561a290b39628cf1aab5f

"""
import os
from pagerduty import RestApiV2Client

<<<<<<< HEAD
=======

>>>>>>> 68b2cb9e09cf23ea25b561a290b39628cf1aab5f
# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# the "from" address has to be valid for a user in your account
from_address = os.environ['PD_FROM_ADDR']

session = RestApiV2Client(api_token, default_from=from_address)
<<<<<<< HEAD
my_log = session.rget('/log_entries')
=======

# get the services in the account, include the integrations
# https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE5Ng-list-services
my_log = session.rget('/log_entries')

# basic output, report with each service followed by its integrations.
# should be easy enough to change to csv or other formats if needed

>>>>>>> 68b2cb9e09cf23ea25b561a290b39628cf1aab5f
print(my_log)
