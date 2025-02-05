#!/bin/bash

## 
# Add a note to an existing incident.
# requires: the incident ID, the API Token for the account, 
# and the From: address
#
# Will return a JSON structure
# Docs:
# https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE1MA-create-a-note-on-an-incident
##

TOKEN=$PD_API_KEY
ADDR=$PD_FROM_ADDR

ID=$1

curl --request POST \
  --url https://api.pagerduty.com/incidents/$ID/notes \
  --header 'Accept: application/vnd.pagerduty+json;version=2' \
  --header 'Authorization: Token token=$TOKEN' \
  --header 'Content-Type: application/json' \
  --header 'From: $ADDR' \
  --data '{
  "note": {
    "content": "Emergency responders are on the scene."
  }
}'
