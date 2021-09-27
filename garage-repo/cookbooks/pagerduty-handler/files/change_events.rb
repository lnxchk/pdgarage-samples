require 'time'
require 'json'
require 'net/http'
require 'uri'
require 'chef/handler'

module PagerDutyTest
  class ChangeEvent < Chef::Handler

    def report

      # if run_status.updated_resources
      #   Chef::Log.info "Resources updated this run:"
      #   run_status.updated_resources.each {|r| Chef::Log.info "#{@line_prefix}#{r.to_s}"}
      # else
      #   Chef::Log.info "No Resources updated this run!"
      # end


      # I want:
      # cookbook_name
      # recipe_name
      # name
      my_resources = Hash.new

      # from run_status.updated_resources
      run_status.updated_resources.each do |r, values|
        # add infor about the changed resoure into a new hash
        # my_resources[r[:cookbook_name]] << r[:cookbook_name][:name]
        puts r.cookbook_name
        puts r.recipe_name
        puts r.name
        puts r.declared_type
        # long_resource = "#{r.cookbook_name}/#{r.recipe_name}/#{r.declared_type}[#{r.name}]"

        (my_resources["'#{r.cookbook_name}::#{r.recipe_name}'"] ||= []) << "#{r.declared_type}[#{r.name}]"

        # my_resources << long_resource

        # my_resources[r.cookbook_name][r.recipe_name] << [r.name]

      end
      puts my_resources
      # You need the integration key from your service.
      # create one at https://ACCOUNT.pagerduty.com/change_events
      service_key = "3.............................e9"
      # service_key = node['pagerduty_handler']['service_key']

      # This is a global API Access Key for your account. An account admin
      # should create it for you at https://ACCOUNT.pagerduty.com/api_keys
      account_token = ".+................pw"

      host = 'events.pagerduty.com'
      port = 443
      path = "/v2/change/enqueue"
      request_path = "https://#{host}:#{port}#{path}"

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
            'build_developer' => "Mandi Walls",
            'updated_resources' => my_resources
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

    end
  end
end
