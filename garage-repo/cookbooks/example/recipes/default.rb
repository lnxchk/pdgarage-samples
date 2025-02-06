# This is a Chef Infra Client recipe file. It can be used to specify resources
# which will apply configuration to a server.
require 'time'

time = Time.now()

log "Welcome to Chef Infra Client, #{node['example']['name']}!" do
  level :info
end

file "/tmp/timer1" do
  content '#{time}'
end

file "/tmp/timer3" do
  content '#{time}'
end
# For more information, see the documentation: https://docs.chef.io/recipes.html
