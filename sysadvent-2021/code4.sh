##
# Change the following pieces:
# the ID must be a valid active incident ID in your account
# Update the token to an API Token for your account
# Update the From header
#
##

ID=..............
curl --request POST \
  --url https://api.pagerduty.com/incidents/$ID/notes \
  --header 'Accept: application/vnd.pagerduty+json;version=2' \
  --header 'Authorization: Token token=.+..................' \
  --header 'Content-Type: application/json' \
  --header 'From: me@myemail.com' \
  --data '{
  "note": {
    "content": "Firefighters are on the scene."
  }
}'

