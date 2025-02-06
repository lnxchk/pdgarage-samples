#!/usr/bin/env bash
# Create an incident on the service passed on the command line.
# You will need the service ID.

TOKEN=$PD_API_KEY
EMAIL=$PD_FROM_ADDR
SERVICE=$1

curl --request POST \
  --url https://api.pagerduty.com/incidents \
  --header 'Accept: application/json' \
  --header "Authorization: Token token=$TOKEN" \
  --header 'Content-Type: application/json' \
  --header "From: $PD_FROM_ADDR" \
  --data "{
  "incident": {
    "type": "incident",
    "title": "The server is on fire.",
    "service": {
      "id": $SERVICE,
      "type": "service_reference"
    },
    "urgency": "high",
    "body": {
      "type": "incident_body",
      "details": "A disk is getting full on this machine. You should investigate what is causing the disk to fill, and ensure that there is an automated process in place for ensuring data is rotated. If data is expected to stay on this disk forever, you should start planning to scale up to a larger disk."
    }
  }
}"
