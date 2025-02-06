#!/usr/bin/env bash
# Get the escalation policies associated with a service
# Includes the full service object and embeds the escalation
# policy objects in the output

# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY

SERVICE=$1

ENDPOINT="/services/$SERVICE?include[]=escalation_policies"

curl -X GET --header 'Content-Type: application/json' \
--url https://api.pagerduty.com/$ENDPOINT \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header "Authorization: Token token=$TOKEN" 

echo
