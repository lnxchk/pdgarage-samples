"""
Update of multiple incidents across all services.
By default it sets all incidents to 'resolved'.
If you want to limit it to some services, update the service_ids array and
add
"service_ids[]": service_ids
to the query parameters 

You'll need a valid API token and from: address in your environment variables

To change the statuses, update the statuses array in the top section.

Pass the service id on the command line or at the prompt.
"""

import os
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

# v1. this multi-update isn't working. see v2 below.
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
    params={'statuses[]': statuses})

for i in incidents:
    i['status'] = 'resolved'

updated_incidents = session.rput('incidents', json=incidents)

print(updated_incidents)

