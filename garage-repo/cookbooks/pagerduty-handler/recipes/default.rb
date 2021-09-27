#
# Cookbook:: pagerduty-handler
# Recipe:: default
#
# Copyright:: 2021, The Authors, All Rights Reserved.
#
require 'time'

time = Time.now()
file "/tmp/timer2" do
  content '#{time}'
end

cookbook_file '/tmp/change_events.rb' do
  source 'change_events.rb'
end

cookbook_file '/tmp/dummy_handler.rb' do
  source 'dummy_handler.rb'
end



# chef_handler 'SimpleReport::UpdatedResources' do
#   source '/tmp/dummy_handler.rb'
#   action :enable
# end

chef_handler 'PagerDutyTest::ChangeEvent' do
  source '/tmp/change_events.rb'
  action :enable
end
