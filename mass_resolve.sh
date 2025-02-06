
#!/usr/bin/env bash
# Resolve multiple incidents in one request.
# Each incident is passed as its own object.

# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY

# valid email for a user in your PagerDuty account
EMAIL=$PD_FROM_ADDR

data=$(cat <<EOF
[{"id": "ID GOES HERE", "type": "incident_reference", "status": "resolved"}, {"id": "ID GOES HERE", "type": "incident_reference", "status": "resolved"}]
EOF
)


echo $data

curl -X POST --header 'Content-Type: application/json' \
--url https://api.pagerduty.com/incidents \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header "From: $PD_FROM_ADDR" \
--header "Authorization: Token token=$TOKEN" \
--data "$data"

echo
