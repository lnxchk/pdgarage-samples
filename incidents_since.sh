# Get the incidents on a particular service for the past day.
# include the total in the output 

# pass the service as the first argument to the script:
# ./incidents_since.sh PMYSERID

# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY


NOW=`date +%FT%T%z`
SINCE=`date -v-1d +%FT%T%z`
S_ID=$1

ENDPOINT="/incidents?service_ids[]=$S_ID&since=$SINCE&until=$NOW&total=true"

curl -X GET --header 'Content-Type: application/json' \
--url https://api.pagerduty.com/$ENDPOINT \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header "Authorization: Token token=$TOKEN" 

echo
