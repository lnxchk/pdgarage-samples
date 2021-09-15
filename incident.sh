# change the token to your token
# change the From: to an email address associated with your acct
# change the service.id to a valid service in your acct

curl -X POST --header 'Content-Type: application/json' \
--url https://api.pagerduty.com/incidents \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header 'From: ********@*******.com' \
--header 'Authorization: Token token=*************' \
--data '{
  "incident": {
    "type": "incident",
    "title": "The server is on fire",
    "service": {
      "id": "P*******",
      "summary": null,
      "type": "service_reference",
      "self": null,
      "html_url": null
    }
  }
}'
echo
