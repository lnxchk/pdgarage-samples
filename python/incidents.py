"""
some playing around with the incidents endpoint

you'll need a valid API token and from: address
"""

from pdpyras import APISession

# example using curl:
# --url 'https://api.pagerduty.com/incidents?date_range=all&urgencies%5B%5D=high&statuses%5B%5D=triggered&include%5B%5D=users&service_ids%5B%5D=.......' \
# --header 'Accept: application/vnd.pagerduty+json;version=2' \
# --header 'Authorization: Token token=.+..................' \
# --header 'Content-Type: application/json'

# set some example parameters to play with
endpoint = "/incidents"
date_range = "all"
urgencies = ['high']
statuses = ['triggered', 'acknowledged']
include = "users"
service_ids = ["SERVICE ID"]

api_token = '.+..................'
session = APISession(api_token, default_from='....@.......')

# query the API for all current incidents on the specified service
current_incidents = session.list_all(
    'incidents',
    params={'service_ids[]': service_ids, 'statuses[]': statuses, 'date_range': date_range}
)

# print(current_incidents)

# query the API for all current incidents assigned to the specified team
team_ids = ['TEAM ID']
team_incidents = session.iter_all(
    'incidents',
    params={'team_ids[]': team_ids, 'statuses[]': statuses, 'date_range': date_range}
)

# for i in team_incidents:
#     print(i['incident_number'])

# query the API for all incidents owned by the specified user
user_ids = ['USER ID']
user_incidents = session.list_all(
    'incidents',
    params={'user_ids[]': user_ids, 'statuses[]': statuses, 'date_range': date_range}
)

# resolve the incidents from the previous query
for i in user_incidents:
    # print(i['incident_number'])
    i['status'] = 'resolved'

updated_incidents = session.rput('incidents', json=user_incidents)

