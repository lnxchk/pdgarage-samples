# Get all schedules on your PagerDuty organization

# Variables
# PD_API_KEY your api key
# PD_FROM_ADDR email address associated with a valid user in your PagerDuty account

# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY

# valid email for a user in your PagerDuty account
EMAIL=$PD_FROM_ADDR

ENDPOINT=/schedules

#cat <<EOF
curl -X GET --header 'Content-Type: application/json' \
--url https://api.pagerduty.com/$ENDPOINT \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header 'From: $EMAIL' \
--header 'Authorization: Token token=$TOKEN' 
#EOF

echo
