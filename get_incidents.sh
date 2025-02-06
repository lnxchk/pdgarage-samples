#!/usr/bin/env bash
# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY


ENDPOINT="/incidents"


curl -X GET --url https://api.pagerduty.com/incidents \
--header "Accept: application/vnd.pagerduty+json;version=2" \
--header "Authorization: Token token=$TOKEN" \
--header "Content-Type: application/json"

echo $data
