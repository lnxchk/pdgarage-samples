# EXAMPLE:
# create a generic event on a service.

# ==========================================
# Documentation:
#
# Usage:
# ./send_event.sh template.json
# will print out the request body
# and the response from the API.
#
# ==========================================

# timestamp for the event
DATE=$(date +%FT%T%z)
# build number if you want to use it
# BUILD_NUMBER=`date +%s`


# event template file
# a local json file that contains the payload of the event type
TEMPLATE=$1

data=$(envsubst < $TEMPLATE)

echo $data

curl -X POST --header 'Content-Type: application/json' \
--url https://events.pagerduty.com/v2/enqueue \
--data "$data"

echo
