"""
Print a week's worth of oncall shifts to a Slack channel.

You will need:
PagerDuty REST API key. See https://support.pagerduty.com/docs/api-access-keys
    environment variable 'PD_API_KEY'
Slack Channel URL. See https://api.slack.com/messaging/webhooks
    environment variable 'SLACK_CHANNEL_URL'
The object id of your Schedule. Available from the URL of that schedule's page in the webui
"""

import json
import os
import requests
from datetime import datetime, timedelta, timezone, date
from pdpyras import APISession

api_token = os.environ['PD_API_KEY']

# initialize the session with the PagerDuty API
session = APISession(api_token)

this_schedule = "POBJECTID"

# your slack webhook url
slack_url = os.environ['SLACK_CHANNEL_URL']
blocks = []
header_block = {
    "type": "header",
    "text": {
        "type": "plain_text",
        "text": "On Call This Week:"
    }
}
blocks.append(header_block)

### Shows the next 7 days
### Schedule to run on Mondays to see the coming week
since = datetime.now()
until = since + timedelta(days=7)
since_time = since.isoformat()
until_time = until.isoformat()


schedule = session.rget(f"/schedules/{this_schedule}?since={since_time}&until={until_time}")

# response_object = json.dumps(schedule, indent=2)
# print(response_object)

for entry in schedule["final_schedule"]["rendered_schedule_entries"]:
    # print(f"{entry["user"]["summary"]} on call from {entry["start"]} until {entry["end"]}")
    begin = datetime.fromisoformat(entry["start"])
    begin_day = begin.strftime("%A")
    begin_hour = begin.strftime("%I %p")
    end = datetime.fromisoformat(entry["end"])
    end_day = end.strftime("%A")
    end_hour = end.strftime("%I %p")
    oncall_string = f"{entry["user"]["summary"]} on call from {begin_day} at {begin_hour} until {end_day} at {end_hour}"

    oncall_block = {
       "type": "section",
       "text": {
           "type": "mrkdwn",
           "text": oncall_string
       }
    }

    blocks.append(oncall_block)

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
