"""
    Send PagerDuty Maintenance Windows to a Slack channel.
    Uses the PagerDuty API and a Slack connection via webhooks.

    requires:
        PagerDuty account and API key to the REST API
        https://support.pagerduty.com/docs/api-access-keys

        Python package pagerduty
        https://github.com/PagerDuty/pagerduty

        Slack workspace and admin access on that space to set
        up an app, or a pre-configured app with a webhook.
        https://api.slack.com/messaging/webhooks

    Other slack connection types are possible, but not what this
    example is set up to support.

"""

import json
import os
import requests
from datetime import datetime
from pagerduty import RestApiV2Client

# auth
# find your PagerDuty api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
# or use a user token key
api_token = os.environ['PD_API_KEY']

# initialize the PagerDuty API session
session = RestApiV2Client(api_token)

# your slack webhook url
slack_url = os.environ['SLACK_CHANNEL_URL']


# query PagerDuty for the maintenance windows
# filter=open will retrieve all windows happening now and all in the future
endpoint = "maintenance_windows?filter=open"

# send the request using the pagerduty session
response = session.rget(endpoint)

# we'll build a json payload to send to the slack webhook
payload = ""

# each piece is a block in the message
# for different formatting, check out this cool Block Kit Builder
# https://app.slack.com/block-kit-builder/T01BC67R125
blocks = []
header_block = {
    "type": "header",
    "text": {
        "type": "plain_text",
        "text": "The following maintenance windows are scheduled:"
    }
}

blocks.append(header_block)

# no current maintenance windows
if not response:
    my_block = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "There are no maintenance windows scheduled"
        }
    }

    blocks.append(my_block)
else:
    today = datetime.today()
    for mw in response:
        # formatting string for making today's windows stand out
        star = ""
        for serv in mw['services']:
            mw_id = mw['id']
            desc = mw['description']
            service = serv['summary']
            link = mw['html_url']
            service_link = serv['html_url']

            start_time = mw['start_time']
            s_time = datetime.strptime(mw['start_time'], "%Y-%m-%dT%H:%M:%S%z")
            s_readable = s_time.strftime("%H:%M %Z")
            if today.date() == s_time.date():
                star = "*Today* "
            else:
                month = s_time.date().strftime('%b')
                star = "{} {}, {}: ".format(month, s_time.day, s_time.year)
            end_time = mw['end_time']
            e_time = datetime.strptime(mw['end_time'], "%Y-%m-%dT%H:%M:%S%z")
            e_readable = e_time.strftime("%H:%M %Z")
            if e_time.timestamp() > today.timestamp() > s_time.timestamp():
                star = "*Happening Now:* "

            my_block = {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ">" + star + "<{}|{}>".format(service_link, service) + " from " + s_readable + " to " + e_readable + " <{}|Click here for info>".format(link)
                }
            }
            blocks.append(my_block)


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
