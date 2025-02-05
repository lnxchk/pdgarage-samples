# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY

# valid email for a user in your PagerDuty account
EMAIL=$PD_FROM_ADDR

ENDPOINT="incidents"

DATA=$(cat <<EOF
{
  "incident": {
    "type": "incident",
    "title": "The server is on fire",
    "assignments": ["mwalls+beth@pagerduty.com"],
    "service": {
      "id": "$SERVICE",
      "summary": null,
      "type": "service_reference",
      "self": null,
      "html_url": null
    }
  }
}
EOF
)


curl -X POST --header 'Content-Type: application/json' \
--url https://api.pagerduty.com/$ENDPOINT \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header "From: $EMAIL" \
--header "Authorization: Token token=$TOKEN" \
--data "$DATA"

echo
