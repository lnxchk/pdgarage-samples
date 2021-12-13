##
# Change the following data pieces:
# update the routing_key in the data
#
##

curl --request POST \
  --url https://events.pagerduty.com/v2/enqueue \
  --header 'Content-Type: application/json' \
  --data '{
  "payload": {
    "summary": "DISK at 99% on machine prod-datapipe03.example.com",
    "timestamp": "2021-12-13T08:42:58.315+0000",
    "severity": "critical",
    "source": "prod-datapipe03.example.com",
    "component": "mysql",
    "group": "prod-datapipe",
    "class": "disk",
    "custom_details": {
      "free space": "1%",
      "ping time": "1500ms",
      "load avg": 0.75
    }
  },
  "event_action": "trigger",
  "routing_key": "................................"
}'

