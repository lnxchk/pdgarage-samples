# create a maintenance window

# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY

# valid email for a user in your PagerDuty account
EMAIL=$PD_FROM_ADDR

ENDPOINT="maintenance_windows"

START_DATE=`date +%FT%T%z`
END_DATE=`date -v +1H +%FT%T%z`
SERVICE="XXXXXXXX"

data=$(cat <<EOF
{
  "maintenance_window": {
    "type": "maintenance_window",
    "start_time": "$START_DATE",
    "end_time": "$END_DATE",
    "description": "Too hot. Working on cooldown",
    "services": [
      {
        "id": "$SERVICE",
        "type": "service_reference"
      }
    ]
  }
}
EOF
)


curl -X POST --header 'Content-Type: application/json' \
--url https://api.pagerduty.com/$ENDPOINT \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header "From: $EMAIL" \
--header "Authorization: Token token=$TOKEN" \
--data "$data"
echo
