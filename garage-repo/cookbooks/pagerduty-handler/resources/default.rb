provides :pagerduty_handler
unified_mode true

property :account_token,
          String

property :service_key,
          String

property :contact,
          String

property :host,
          String,
          default: 'events.pagerduty.com'

property :port,
          Integer,
          default: 443

property :api_path,
          String,
          default: "/v2/change/enqueue"

property :summary,
          String,
          default: 'Changed Resources from Chef-Client Run'

property :name,
          String,
          name_property: true


action :enable do
  chef_handler 'PagerDuty::ChangeEvent' do
    source 'change_events.rb'
    action :enable
  end
end
