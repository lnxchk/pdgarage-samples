#!/usr/bin/env bash
# Get on call responder by schedule
# In comments: get on call shift by user

# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY

# valid email for a user in your PagerDuty account
EMAIL=$PD_FROM_ADDR

ID=$1

#ENDPOINT="oncalls?user_ids[]=$ID"
ENDPOINT="oncalls?schedule_ids[]=$ID"

curl -X GET --header 'Content-Type: application/json' \
--url https://api.pagerduty.com/$ENDPOINT \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header "From: $EMAIL" \
--header "Authorization: Token token=$TOKEN" 

echo
