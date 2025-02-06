#!/usr/bin/env bash
# Resolve an incident
# Pass the incident ID on the command line

# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY

# valid email for a user in your PagerDuty account
EMAIL=$PD_FROM_ADDR

INCIDENT=$1
data=$(cat <<EOF
{
    "incident": {
        "type": "incident_reference",
        "status": "resolved"
    }
}
EOF
)
ENDPOINT="/incidents/$INCIDENT"

curl -X GET --header 'Content-Type: application/json' \
--url https://api.pagerduty.com/$ENDPOINT \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header "From: $EMAIL" \
--header "Authorization: Token token=$TOKEN" \
--data "$data"

echo
