"""
    Send PagerDuty Oncall Responder to a Slack channel.
    Uses the PagerDuty API and a Slack connection via webhooks.

    requires:
        PagerDuty account and API key to the REST API
        https://support.pagerduty.com/docs/api-access-keys

        Python package pdpyras
        https://github.com/PagerDuty/pdpyras

        Slack workspace and admin access on that space to set
        up an app, or a pre-configured app with a webhook.
        https://api.slack.com/messaging/webhooks

    Other slack connection types are possible, but not what this
    example is set up to support.

"""

import json
import os
import requests
from datetime import datetime, timedelta, timezone
from pdpyras import APISession

# auth
# find your PagerDuty api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
# or use a user token key
api_token = os.environ['PD_API_KEY']

# initialize the PagerDuty API session
session = APISession(api_token)

# your slack webhook url
slack_url = os.environ['SLACK_CHANNEL_URL']

blocks = []
header_block = {
    "type": "header",
    "text": {
        "type": "plain_text",
        "text": "Oncall Now:"
    }
}
blocks.append(header_block)

# # since_time for the overrides window
# until_time = datetime.now(timezone.utc)
# since_time = until_time - timedelta(minutes=1)
until_time = datetime.now(timezone.utc)
since_time = until_time - timedelta(minutes=1)

get_scheds = session.rget("/schedules")
for sched in get_scheds:
    sched_id = sched['id']
    sched_name = sched['summary']

    # request individual schedule from the sched_id
    # get_this_sched = session.rget("/schedules/{}/users?since={}&until={}".format(sched_id, since_time, until_time))
    get_this_sched = session.rget("/oncalls?schedule_ids[]={}".format(sched_id))
    try:
        # user = get_this_sched[0]['name']
        user = get_this_sched[0]['user']['summary']
    except IndexError:
        user = "No Current Oncall"

    # query PagerDuty for the overrides
    override_endpoint = "/schedules/{}/overrides?since={}&until={}".format(sched_id, since_time, until_time)

    # send the request using the pdpyras session
    overrides = session.rget(override_endpoint)
    print(overrides)

    # if overrides['overrides']:
        # if there are overrides, figure them out here
        # otherwise, default to the main on-call
        # print(overrides)
        # or_object = json.dumps(overrides, indent=2)
        # print(or_object)
        # user = user + " Override"

    oncall_string = "{} is oncall for schedule {}".format(user, sched_name)
    print(oncall_string)
    # user for the current schedule
    oncall_block = {
       "type": "section",
       "text": {
           "type": "mrkdwn",
           "text": oncall_string
       }
    }

    blocks.append(oncall_block)


# we'll build a json payload to send to the slack webhook
# payload = ""

# build the json payload
payload = {
    "blocks": blocks
}
j_payload = json.dumps(payload)

# create and send the request to the slack webhook url
headers = {"Content-Type": "application/json"}
sent_msg = requests.post(slack_url, headers=headers, data=j_payload)
sent_msg.raise_for_status()
print(sent_msg.text)
