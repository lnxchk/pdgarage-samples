#!/usr/bin/env bash
# get the entries in a specific on call schedule for the last 30 days
# pass the schedule id on the command line

# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY

# valid email for a user in your PagerDuty account
EMAIL=$PD_FROM_ADDR

SCHEDULE_ID=$1
SINCE=`date -v-30d +%FT%T%z`

ENDPOINT="schedules/${SCHEDULE_ID}&since=${SINCE}"

echo $ENDPOINT

curl -X GET --header 'Content-Type: application/json' \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header "From: $FROM" \
--header "Authorization: Token token=$TOKEN" \
--url "https://api.pagerduty.com/$ENDPOINT"

echo
