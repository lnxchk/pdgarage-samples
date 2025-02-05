# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY

# valid email for a user in your PagerDuty account
EMAIL=$PD_FROM_ADDR

ENDPOINT="services/P8TJ5H9"
SERVICE_ID=$1
$EP_ID=$2
data=$(cat << EOF
{
  "service": {
    "type": "service",
    "id": $SERVICE_ID,
    "escalation_policy": {
      "id": $EP_ID,
      "type": "escalation_policy_reference"
    },
    "incident_urgency_rule": {
      "type": "constant",
      "urgency": "high"
    }
  }
}
EOF
)

curl -X PUT --header 'Content-Type: application/json' \
--url https://api.pagerduty.com/$ENDPOINT \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header "From: $EMAIL" \
--header "Authorization: Token token=$TOKEN" \
--data "$data"

echo
