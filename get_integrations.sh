#!/usr/bin/env bash
# Get all information for a specific service, including information on all integrations
# Pass the service ID on the command line.

# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY

# valid email for a user in your PagerDuty account
EMAIL=$PD_FROM_ADDR
SERVICE=$1

ENDPOINT="services/$SERVICE?include[]=integrations"

curl -X GET --header 'Content-Type: application/json' \
--url https://api.pagerduty.com/$ENDPOINT \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header "From: $EMAIL" \
--header "Authorization: Token token=$TOKEN" 

echo
