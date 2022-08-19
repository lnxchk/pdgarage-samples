"""
"""

import sys
import os
from pdpyras import APISession

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = APISession(api_token)

# you can pass the service ID on the command line or enter it at the prompt
if len(sys.argv) < 2:
    my_opt_1 = input("Which schedule? ")
else:
    my_opt_1 = str(sys.argv[1])

if len(sys.argv) < 3:
    my_opt_2 = input("Start timestamp: ")
else:
    my_opt_2 = str(sys.argv[2])


print()

endpoint = "/schedules/{}?since={}".format(my_opt_1, my_opt_2)
# basic output, report with each service followed by its integrations.
# For custom change event integrations, print the code. This is stored in the platform as-is.
response = session.rget(endpoint)

print(response)
