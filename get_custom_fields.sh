#!/usr/bin/env bash
# get the custom fields on a specific incident
# pass the incident ID on the command line

# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY
INCIDENT=$1

ENDPOINT="incidents/$INCIDENT/custom_fields"

curl -X GET --header 'Content-Type: application/json' \
--url https://api.pagerduty.com/$ENDPOINT \
--header "Authorization: Token token=$TOKEN" 


echo
