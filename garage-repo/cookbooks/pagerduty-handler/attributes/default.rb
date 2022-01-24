default['pagerduty_handler']['account_token'] = ".+................pw"
default['pagerduty_handler']['service_key'] = "3..............................9"

default['pagerduty_handler']['host'] = 'events.pagerduty.com'
default['pagerduty_handler']['port'] = 443
default['pagerduty_handler']['api_path'] = "/v2/change/enqueue"

default['pagerduty_handler']['summary'] = "Changed Resources from Chef-Client Run"
default['pagerduty_handler']['contact'] = "me@example.com"

template 'destination_path' do
  source 'source_file'
  action :create
end
