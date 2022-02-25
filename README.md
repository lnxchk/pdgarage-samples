Sample projects for PagerDuty Garage

Join us on Twitch!
* Mondays at 10am Eastern
* Fridays at 4pm Eastern

[PDCommunity](https://twitch.tv/pdcommunity) and [PagerDuty](https://twitch.tv/pagerduty)

Sample Files in this project:

* **change_event.sh** (September 10): Shell script to create change events on a PagerDuty service. To use this script, add your account API Key as the TOKEN and your service integration key as the KEY.

* **change_events.rb** (September 13, 20): Ruby script to create change events on a PagerDuty service. Similar to the shell script above, change the *service_key* and *account_token* variables for your account.

* **incident.sh**: Shell script to create a single incident on a service. To use this script, change the token to be your api_key, the from: address to an email address associated with your account, and the ID of the service to a service in your account.

* **garage-repo**: Chef / Cinc repo. Project: Create a *chef_handler* that will push information about all changed resources in a Chef / Cinc run to a PagerDuty change event.

* **python**: some python scripts for working with the API. These make use of the pdpyras library https://github.com/PagerDuty/pdpyras
  * Environment variables:
    * PD_API_KEY: valid API key for the PagerDuty API
    * PD_FROM_ADDR: valid from address that is in your account
