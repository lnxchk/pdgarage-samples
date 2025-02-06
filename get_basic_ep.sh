#!/usr/bin/env bash
# get all the escalation policies on the account


TOKEN=$PD_API_KEY

curl --request GET \
  --url https://api.pagerduty.com/escalation_policies \
  --header 'Accept: application/json' \
  --header "Authorization: Token token=$TOKEN" \
  --header 'Content-Type: application/json'