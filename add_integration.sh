# Add an integration to an existing service
# The example here uses Elastic.

# for a list of integration vendors, see the 
# docs for the /vendors endpoint
# https://developer.pagerduty.com/api-reference/d2aa663abec79-list-vendors

# Variables
# PD_API_KEY your key
# PD_FROM_ADDR an email address associated with a valid PagerDuty user on your account
# $1 pass the id of the service on the command line

# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY

# valid email for a user in your PagerDuty account
EMAIL=$PD_FROM_ADDR

SERVICE_ID=$1

ENDPOINT="services/$SERVICE_ID/integrations"

DATA=$(cat <<EOF
{
  "integration": {
    "type": "app_event_transform_inbound_integration",
    "name": "Alerts from Elastic",
    "service": {
      "id": "$SERVICE_ID",
      "type": "service_reference"
    },
    "vendor": {
      "type": "vendor_reference",
      "id": "PULN1LU"
    }
  }
}
EOF
)

# echo "$DATA" | jq
echo

curl -X POST --header 'Content-Type: application/json' \
--url https://api.pagerduty.com/$ENDPOINT \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header "From: $EMAIL" \
--header "Authorization: Token token=$TOKEN" \
--data "$DATA"

echo