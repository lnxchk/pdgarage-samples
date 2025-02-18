"""
Query the /users/ endpoint in two ways

Iterate through all users to find the user you want, or use the query option
"""

import sys
import os
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

# you can pass the query string on the command line or enter it at the prompt
if len(sys.argv) < 2:
    this_name = input("Which name query? ")
else:
    this_name = str(sys.argv[1])

print()

endpoint = "/users"
print(endpoint)
# basic output, report with each service followed by its integrations.
# For custom change event integrations, print the code. This is stored in the platform as-is.

# response = session.iter_all(endpoint)
for user in session.iter_all(endpoint):
	if this_name.lower() in user['name'].lower():
		print(user['id'], user['email'], user['name'])

print()

# now use the query function of the endpoint:
# the query option is case insensitive by default
endpoint = "/users?query={}".format(this_name)
print(endpoint)
for user in session.iter_all(endpoint):
	print(user['id'], user['email'], user['name'])

