# EXAMPLE:
# create a generic change event on a service.

# ==========================================
# Documentation:
# https://support.pagerduty.com/docs/change-events
# https://developer.pagerduty.com/api-reference/reference/events-v2/openapiv3.json/paths/~1change~1enqueue/post
#
# Usage:
# ./change_event.sh 
# will print out the request body
# copy and past on the command line
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
KEY=""

data=$(cat <<EOF
  {
    "routing_key": "$KEY",
    "payload": {
      "summary": "Build Success: Build has Passed.",
      "timestamp": "$DATE",
      "source": "amazing-build-pipeline-thing",
      "custom_details": {
        "build_state": "passed",
        "build_number": "$BUILD_NUMBER",
        "build_developer": "Jill Developer"
      }
    }
  }
EOF
)


curl -X POST --header 'Content-Type: application/json' \
--url https://events.pagerduty.com/v2/change/enqueue \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header 'Authorization: Token token=$TOKEN' \
--data "$data"

echo
