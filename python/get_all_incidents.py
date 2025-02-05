"""
some playing around with the incidents endpoint

you'll need a valid API token and from: address
"""

import os
import json
from datetime import datetime, timedelta
from pagerduty import RestApiV2Client

# example using curl:
# --url 'https://api.pagerduty.com/incidents?date_range=all&urgencies%5B%5D=high&statuses%5B%5D=triggered&include%5B%5D=users&service_ids%5B%5D=.......' \
# --header 'Accept: application/vnd.pagerduty+json;version=2' \
# --header 'Authorization: Token token=.+..................' \
# --header 'Content-Type: application/json'

# set some example parameters to play with
endpoint = "/incidents"
urgencies = ['high']
statuses = ['triggered']
include = "users"
team_ids = ["XXXXXXX"]

api_token = os.environ['PD_API_KEY']
from_addr = os.environ['PD_FROM_ADDR']
session = RestApiV2Client(api_token, default_from=from_addr)


def incidents_at_time(since_time, until_time, offset):
    # query the API for all current incidents on the specified service
    # incidents = session.list_all('incidents', params={'since':since_time, 'until':until_time, 'limit': 10})
    incidents = session.request('get', 'incidents', params={'since':since_time,'until':until_time,'limit':10,'offset':offset})

    return incidents


def print_my_incidents(incident_list):
    for incident in incident_list:
        print(incident['id'],incident['resolved_at'])


def main():
    until_time = datetime.utcnow().date()
    since_time = until_time - timedelta(30)
    month = 0
    while month < 12:

        my_incidents = incidents_at_time(since_time, until_time,0)
        # print(my_incidents.text)
        incident_object = json.loads(my_incidents.text)
        # print(incident_object['limit'])
        print_my_incidents(incident_object['incidents'])
        # print(incident_object['more'])
        while incident_object['more']: 
            # print("getting next page")
            new_offset = incident_object['offset'] + incident_object['limit']
            new_incidents = incidents_at_time(since_time, until_time, new_offset)
            incident_object = json.loads(new_incidents.text)
            print_my_incidents(incident_object['incidents'])

        # for incident in my_incidents:
        #    print(incident['id'], incident['resolved_at'])

        until_time = since_time
        since_time = since_time - timedelta(30)
        month += 1


if __name__ == "__main__":
    main()