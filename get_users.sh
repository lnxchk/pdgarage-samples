#!/usr/bin/env bash
# Get the users on a team

# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY

TEAM=$1

ENDPOINT="users?team_ids[]=$TEAM&total=true"

curl -X GET --header 'Content-Type: application/json' \
--url https://api.pagerduty.com/$ENDPOINT \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header "Authorization: Token token=$TOKEN" 

echo
