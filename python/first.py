
import os
from pdpyras import APISession


api_token = os.environ['PD_API_KEY']


user = "USER ID"
session = APISession(api_token)

# query the API and get the users in our PD account
response = session.get('/users/{}'.format(user))
user = None

if response.ok:
    user = response.json()['user']
    # print(user)

for user in session.iter_all('users'):
    print(user['id'], user['email'], user['name'])

# query the API for incidents on a particular service
# incident = session.get('/incidents/{}'.format("PWU7CM6"))

# if response.ok:
#     my_incident = response.json()['incidents']
#     print(my_incident)
# for inc in session.iter_all('')


# query the API for incidents owned by specific users that are acknowledged
incidents = session.list_all(
    'incidents',
    params={'user_ids[]': [user], 'statuses[]': ['acknowledged']}
)

print(incidents)

# TODO: protect this loop in the event there are no incidents on the acct

# update the acknowledged incidents to resolved and push back to the API
for i in incidents:
    i['status'] = 'resolved'
    print(i)

# update to a valid from address:
updated_incidents = session.rput('incidents', json=incidents, headers={"From": "me@domain.com"})
