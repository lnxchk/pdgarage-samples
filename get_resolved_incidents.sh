#!/usr/bin/env bash
# Get all resolved incidents on a given service in the last 30 days

# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY

NOW=`date +%FT%T%z`
SINCE=`date -v-30d +%FT%T%z`

SERVICE=$1
STATUSES="resolved"

ENDPOINT="/incidents?service_ids[]=$SERVICE&since=$SINCE&until=$NOW&statuses[]=$STATUSES"

curl -X GET --header 'Content-Type: application/json' \
--url "https://api.pagerduty.com/$ENDPOINT" \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header "Authorization: Token token=$TOKEN"

echo
