require 'time'
require 'json'
require 'net/http'
require 'uri'

# You need the integration key from your service.
# create one at https://ACCOUNT.pagerduty.com/change_events
service_key = "3b3..........................ae9"

# This is a global API Access Key for your account. An account admin
# should create it for you at https://ACCOUNT.pagerduty.com/api_keys
account_token = ".+................BQ"

HOST = 'events.pagerduty.com'
PORT = 443
PATH = "/v2/change/enqueue"
request_path = "https://#{HOST}:#{PORT}#{PATH}"

# create the payload.
payload = {
  'routing_key' => service_key,
  'payload' => {
    'summary' => "Summary goes here success",
    'timestamp' => Time.now.strftime("%FT%T%z"),
    'source' => "Practice Change Events Ruby Script",
    'custom_details' => {
      'build_state' => "passed",
      'build_number' => Time.now.to_i,
      'build_developer' => "Mandi Walls"
    }
  }
}

# build the request
uri = URI(request_path)
puts uri.hostname
req = Net::HTTP::Post.new(uri)
req['Accept'] = "application/vnd.pagerduty+json;version=2"
req['Content-Type'] = "application/json"
req['Authorization'] = "Token token=#{account_token}"
req.body = payload.to_json

response = Net::HTTP.start(uri.hostname) { |http|
  http.request(req)
}

case response
when Net::HTTPSuccess, Net::HTTPRedirection
  # OK
else
  puts "Request Failed: #{response.body}"
end
