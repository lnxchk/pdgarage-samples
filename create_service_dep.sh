#!/usr/bin/env bash
# Create a service dependency
# The supporting service is passed as the first argument 
# The dependent service is passed as the second argument
# both require the service ID 

# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY

# valid email for a user in your PagerDuty account
EMAIL=$PD_FROM_ADDR

sup_service=$1
dep_service=$2

echo "$dep_service will depend on $sup_service"

data=$(cat <<EOF
  {
    "relationships": [
     {
      "supporting_service": {
	"id": "$sup_service",
        "type": "service"
      },
      "dependent_service": {
        "id": "$dep_service",
        "type": "business_service"
      }
     }
    ]
  }
EOF
)

curl -X POST --header 'Content-Type: application/json' \
--url https://api.pagerduty.com/service_dependencies/associate \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header "Authorization: Token token=$TOKEN" \
--data "$data"
echo
