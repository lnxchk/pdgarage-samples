##
# Change the following data piece
# update the routing_key in the data section
#
## 

curl --request POST \
  --url https://events.pagerduty.com/v2/change/enqueue \
  --header 'Content-Type: application/json' \
  --data '{
  "routing_key": "................................",
  "payload": {
    "summary": "Build Success: Increase snapshot create timeout to 30 seconds",
    "timestamp": "2021-12-13T09:42:58.315+0000",
    "source": "prod-build-agent-i-0b148d1040d565540",
    "custom_details": {
      "build_state": "passed",
      "build_number": "220",
      "run_time": "1236s"
    }
  }
}'

