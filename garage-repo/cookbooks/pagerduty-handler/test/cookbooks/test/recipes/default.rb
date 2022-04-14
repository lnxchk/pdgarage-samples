pagerduty_handler 'ChangeEvent' do
  account_token node['pagerduty']['account_token']
  service_key node['pagerduty']['service_key']
  contact node['pagerduty']['contact_email']
end
