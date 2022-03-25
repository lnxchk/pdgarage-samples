"""
Multiple update of incidents. By default it sets all incidents on one service to 'resolved'

You'll need a valid API token and from: address in your environment variables

To change the statuses, update the statuses array in the top section.

Pass the service id on the command line or at the prompt.
"""

import os
import sys
# import json
from pdpyras import APISession

# set some example parameters to play with
endpoint = "/incidents"
date_range = "all"
urgencies = ['high']
statuses = ['triggered', 'acknowledged']
include = "users"
service_ids = []

api_token = os.environ['PD_API_KEY']
from_addr = os.environ['PD_FROM_ADDR']
session = APISession(api_token, default_from=from_addr)

# you can pass the service ID on the command line or enter it at the prompt
if len(sys.argv) < 2:
    this_service = input("Which service? ")
else:
    this_service = str(sys.argv[1])

service_ids.append(this_service)

# json_build = []
# # query the API for all current incidents on the specified service
# for current_incident in session.iter_all(
#     'incidents',
#     params={'statuses[]': statuses}
# ):
#     # print("Current incident id is: {}".format(current_incident['id']))
#     my_id = current_incident['id']
#     id_dict = {'id': my_id, 'type': 'incident_reference', 'status': 'resolved'}
#     json_build.append(id_dict)
# print(json_build)
#
# json_payload = json.dumps(json_build)
# print(json_payload)
# session.rput(
#     "incidents",
#     json=json_payload
# )


# v2
incidents = session.list_all(
    'incidents',
    params={'statuses[]': statuses, 'service_ids[]': service_ids})

for i in incidents:
    i['status'] = 'resolved'


# print(incidents)
#
updated_incidents = session.rput('incidents', json=incidents)

# print(updated_incidents)

