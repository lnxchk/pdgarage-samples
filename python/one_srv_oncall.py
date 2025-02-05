"""
Service Integrations Audit
with Custom Change Events Code

This script will query your PagerDuty account for all integrations
on a single service.

If the service has a custom change event transform integration,
print the code of that integration.

For more on integrations, see the Knowledge Base at
https://support.pagerduty.com/docs/services-and-integrations

For more on the custom change event transform capability,
https://developer.pagerduty.com/docs/ZG9jOjExMDI5NTgz-custom-change-event-transformer
"""

import sys
import os
import json
from pagerduty import RestApiV2Client
from datetime import datetime, timedelta, timezone

# since_time for the overrides window
since = datetime.now(timezone.utc)
until = since + timedelta(minutes=1)
since_time = since.isoformat()
until_time = until.isoformat()


def get_oncall_from_sched(sched_id):
    # make a session call to request the schedule using the id
    sched = session.rget("/schedules/{}?since={}&until={}".format(sched_id, since_time, until_time))
    try:
        s_oncall = sched['final_schedule']['rendered_schedule_entries'][0]['user']['summary']
    except IndexError:
        s_oncall = "No One"
    return s_oncall


# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)

# you can pass the service ID on the command line or enter it at the prompt
if len(sys.argv) < 2:
    this_service = input("Which service? ")
    print()
else:
    this_service = str(sys.argv[1])

# get the service object, include the escalation policy info
my_service = session.rget('/services/{}?include[]=escalation_policies'.format(this_service))
# these two lines will dump the service object as json
# j_service = json.dumps(my_service, indent=2)
# print(j_service)

rule_level = 1
oncalls = {}
for rule in my_service['escalation_policy']['escalation_rules']:
    for target in rule['targets']:
        if target['type'] == "schedule_reference":
            # print("this rule is a schedule: {}".format(target['summary']))
            person = get_oncall_from_sched(target['id'])
        elif target['type'] == "user_reference":
            # print("this rule is a person: {}".format(target['summary']))
            person = target['summary']
        if rule_level not in oncalls:
            oncalls[rule_level] = person
        else:
            oncalls[rule_level] = oncalls[rule_level] + ", " + person

    rule_level += 1

# print(oncalls)
print("For Service: {}".format(my_service['summary']))
for rule in sorted(oncalls):
    print("Level {}: {}".format(rule, oncalls[rule]))
