# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY

# valid email for a user in your PagerDuty account
EMAIL=$PD_FROM_ADDR


TODAY=`date +%FT%T%z`
LATER=`date -v +1m +%FT%T%z`

ENDPOINT="https://api.pagerduty.com/schedules/PJ3GLH7/overrides?since=$TODAY&until=$LATER"

curl -X GET --header 'Content-Type: application/json' \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header "Authorization: Token token=$TOKEN" \
--url $ENDPOINT
echo
