# EXAMPLE:
# create a generic event on a service.

# ==========================================
# Documentation:
#
# Usage:
# ./send_event.sh
# will print out the request body
# and the response from the API.
#
# ==========================================

# timestamp for the event
DATE=`date +%FT%T%z`
# build number using time so increments
BUILD_NUMBER=`date +%s`

# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY

# valid email for a user in your PagerDuty account
EMAIL=$PD_FROM_ADDR

# integration key
# this is a SERVICE LEVEL integration
# you need a different key for each destination service
# https://youraccount.pagerduty.com/change-events
KEY=$PD_ROUTE_KEY


#data=$(cat <<EOF
#  {
#    "routing_key": "$KEY",
#    "payload": {
#      "summary": "Service 'nginx' is DOWN",
#      "severity": "critical",
#      "source": "host2.example.com"
#    },
#    "event_action": "trigger"
#  }
#EOF
#)
data=$(cat <<EOF
{
  "payload": {
    "summary": "nginx is not running on machine prod-datapipe03.example.com",
    "severity": "critical",
    "source": "prod-datapipe03.example.com",
    "component": "nginx",
    "group": "prod-datapipe",
    "class": "service"
  },
  "routing_key": "$KEY",
  "event_action": "trigger",
  "client": "Sample Monitoring Service",
  "client_url": "https://monitoring.service.com"
}
EOF
)
echo $data

curl -X POST --header 'Content-Type: application/json' \
--url https://events.pagerduty.com/v2/enqueue \
--data "$data"

echo
