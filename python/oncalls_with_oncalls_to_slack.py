"""
    Send PagerDuty Oncall Responder to a Slack channel.
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
from pagerduty import RestApiV2Client

# auth
# find your PagerDuty api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
# or use a user token key
api_token = os.environ['PD_API_KEY']

# initialize the session with the PagerDuty API
session = RestApiV2Client(api_token)

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
# all_eps is going to capture just the escalation policy id, summary, and oncalls at each rule
all_eps = {}

# this is going to request the oncalls based on active escalation policies
all_oncalls = session.rget("/oncalls")

for oncall in all_oncalls:
    # things we can get back:
    # more than one person on call for an escalation policy - as individuals
    # a schedule included in the ep, and the current oncall for that schedule
    # more than one layer in an escalation policy
    ep_id = oncall['escalation_policy']['id']

    # the escalation policy is already included, add another person
    if ep_id not in all_eps:
        all_eps[ep_id] = {
            "summary": oncall['escalation_policy']['summary'],
            "html_url": oncall['escalation_policy']['html_url'],
            "levels": {}
        }
    esc_level = oncall['escalation_level']
    if esc_level not in all_eps[ep_id]['levels']:
        all_eps[ep_id]['levels'][esc_level] = {"people": oncall['user']['summary']}
    else:
        all_eps[ep_id]['levels'][esc_level]["people"] = all_eps[ep_id]['levels'][esc_level]["people"] + ", " + oncall['user']['summary']

for ep in all_eps:
    # build the message block for this escalation policy
    msg_str = "*<{}|{}>* ".format(all_eps[ep]['html_url'], all_eps[ep]['summary'])
    for level in sorted(all_eps[ep]['levels'].keys()):
        msg_str = msg_str + "| *Level {}*: {} ".format(level, all_eps[ep]['levels'][level]['people'])
    msg_block = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": msg_str
        }
    }
    blocks.append(msg_block)


j_all_eps = json.dumps(all_eps, indent=2)
# print(j_all_eps)
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
