#!/usr/bin/env bash
# get a list of all extensions installed on your PagerDuty account.

# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY
curl -X GET --header 'Content-Type: application/json' \
--url https://api.pagerduty.com/extensions \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header "Authorization: Token token=$TOKEN" 

echo
