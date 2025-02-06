#!/usr/bin/env bash
# Get the first page of incidents on an account
# Pagination is available.
# basic queries will top out at 10,000 incidents with pagination

TOKEN=$PD_API_KEY

curl --request GET \
  --url https://api.pagerduty.com/incidents?date_range=all \
  --header 'Accept: application/json' \
  --header "Authorization: Token token=$TOKEN" \
  --header 'Content-Type: application/json'