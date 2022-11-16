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
# converting away from pdpyras because overrides isn't working
# from pdpyras import APISession

# auth
# find your PagerDuty api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
# or use a user token key
api_token = os.environ['PD_API_KEY']

# your slack webhook url
slack_url = os.environ['SLACK_CHANNEL_URL']

# set up requests components
BaseURL = "https://api.pagerduty.com/"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/vnd.pagerduty+json;version=2",
    "Authorization": "Token token={}".format(api_token)
}

blocks = []
header_block = {
    "type": "header",
    "text": {
        "type": "plain_text",
        "text": "Oncall Now:"
    }
}
blocks.append(header_block)

# since_time for the overrides window
since = datetime.now(timezone.utc)
until = since + timedelta(minutes=1)
since_time = since.isoformat()
until_time = until.isoformat()

sched_response = requests.get("{}/schedules".format(BaseURL), headers=headers)
get_scheds = sched_response.json()

for sched in get_scheds['schedules']:
    sched_id = sched['id']
    sched_name = sched['summary']
    # request individual schedule from the sched_id
    get_this_sched = requests.get("{}/oncalls?schedule_ids[]={}".format(BaseURL, sched_id), headers=headers)
    this_sched = get_this_sched.json()
    try:
        oncall = this_sched['oncalls']
        user = oncall[0]['user']['summary']
    except IndexError:
        user = "No One"

    # query PagerDuty for the overrides
    querystring = {"since": since_time, "until": until_time}
    override_endpoint = "{}/schedules/{}/overrides".format(BaseURL, sched_id)
    overrides = requests.get(override_endpoint, headers=headers, params=querystring).json()
    if overrides['overrides']:
        # if there are overrides, figure them out here
        # otherwise, default to the main on-call
        e_time = datetime.strptime(overrides['overrides'][0]['end'], "%Y-%m-%dT%H:%M:%S%z")
        e_readable = e_time.strftime("%H:%M %Z")
        user = user + " (Override until {})".format(e_readable)

    oncall_string = "{} is oncall for {}".format(user, sched_name)
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
slack_headers = {"Content-Type": "application/json"}
sent_msg = requests.post(slack_url, headers=slack_headers, data=j_payload)
sent_msg.raise_for_status()
print(sent_msg.text)
