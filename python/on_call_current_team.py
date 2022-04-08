"""
Get the users who are currently on call in your PagerDuty account.

Queries for all schedules, lists the current on-call and the
teams represented on the schedules.

Future work could include linking the users with their team, but
any user can belong to multiple teams.
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
# if len(sys.argv) < 2:
#     this_service = input("Which service? ")
# else:
#     this_service = str(sys.argv[1])

print()
endpoint = "/schedules"
schedule = session.rget(endpoint)
# print(schedule)
for sched in schedule:
    print(sched['id'], sched['summary'])
    print("\t", sched['users'][0]['id'], sched['users'][0]['summary'])
    for t in sched['teams']:
        print("\t", t['id'], t['summary'])
