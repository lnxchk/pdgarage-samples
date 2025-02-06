#
# Cookbook:: pagerduty-handler
# Spec:: default
#
# Copyright:: 2021, The Authors, All Rights Reserved.

require 'spec_helper'

describe 'pagerduty-handler' do
  step_into :pagerduty_handler
  platform 'ubuntu'

  context 'Enable the PagerDuty handler' do
    recipe do
      pagerduty_handler 'ChangeEvent' do
        account_token 'foo'
        service_key 'bar'
        contact 'foo@bar.com'
      end
    end
  end

  it { is_expected.to render_file().with_content('') }
end
