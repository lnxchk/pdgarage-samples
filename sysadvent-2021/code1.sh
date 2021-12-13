##
# Update these data pieces:
# Token in the headers
# From email address in the headers
# Service ID in the data body of the payload
##

curl -X POST --header 'Content-Type: application/json' \
--url https://api.pagerduty.com/incidents \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header 'Authorization: Token token=.+..................' \
--header 'From: me@myemail.com' \
--data '{
  "incident": {
    "type": "incident",
    "title": "Too many blocked requests",
    "service": {
      "id": ".......",
      "summary": null,
      "type": "service_reference",
      "self": null,
      "html_url": null
    },
    "body": {
      "type": "incident_body",
      "details": "The service queue is full. Requests are no longer being fulfilled."
    }
  }
}'

