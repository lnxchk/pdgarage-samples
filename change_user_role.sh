# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY

# valid email for a user in your PagerDuty account
EMAIL=$PD_FROM_ADDR

TEAMID=$PD_TEAM_ID
USERID=$PD_USER_ID

ENDPOINT="/teams/$TEAMID/users/$USERID"

curl -X PUT --header 'Content-Type: application/json' \
--url https://api.pagerduty.com/$ENDPOINT \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header "From: $EMAIL" \
--header "Authorization: Token token=$TOKEN" \
--data '{
         "role": "responder"
       }'
echo
