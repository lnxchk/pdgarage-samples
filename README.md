# Sample scripts for accessing parts of the PagerDuty API
Many of these pieces were inspired by questions in our [Community Forums](https://community.pagerduty.com)

None of these are *guaranteed* to work. Many of them do; they are intended as examples, not solutions.

## Sample files in this project:

### Bash
Unless otherwise specified, these scripts require two environment variables:
* `PD_API_KEY`: your PagerDuty [API Key](https://developer.pagerduty.com/docs/authentication)
* `PD_FROM_ADDR`: an email address associated with a PagerDuty user account. This will attribute any changes to that user.

Most of these scripts take arguments on the command line if arguments are needed. Because the return document will be JSON, you can pipe the output to a parser like `jq` to improve human readability. 

* **add_integration.sh**: Create an integration on a service. The service ID is passed on the command line. See the vendor documentation to find the appropriate vendor object for your integration.
* **all_schedules.sh**: Get all schedules on your account.
* **bash_template.sh**: Basic template for bash scripts.
* **change_event.sh**: Create change events on a PagerDuty service. Pass the integration key on the command line.
* **create_incident.sh**: Script to create an incident on a service. Pass the service ID on the command line.
* **create_service_dep.sh**: Create a service dependency for the service graph. Pass the supporting service as the first command line argument and the dependent service as the second argument. Use the service IDs.
* **get_all_sched.sh**: Get all the users on a specific oncall schedule. Pass the schedule ID on the command line.
* **get_basic_ep.sh**: Get all the escalation policies on an account. Requires only `PD_API_KEY`.
* **get_basic_incidents.sh**: Get all open incidents on an account. Includes an example for using the options to the incidents query. Does not include pagination, see API docs for more details. Requires only `PD_API_KEY`.
* **get_custom_fields.sh**: Get the custom fields applied to a specific incident. Pass the incident ID on the command line.  Requires only `PD_API_KEY`.
* **get_escalation.sh**: Get a specific escalation policy. Pass the escalation policy ID on the command line. Requires only `PD_API_KEY`.
* **get_extensions.sh**: Get a list of the extensions installed on your PagerDuty account. Requires only `PD_API_KEY`.
* **get_incident.sh**: Get a single incident. Pass the incident ID on the command line. 
* **get_incidents.sh**: Similar to `get_basic_incidents.sh` but does not include an example for the query options.
* **get_incsort.sh**: Similar to `get_basic_incidents.sh` and `get_incidents.sh`. Includes the syntax to use the `sort` option.
* **get_integrations.sh**: Get the integrations on a specified service. Pass the service ID on the command line. Requires only `PD_API_KEY`.
* **get_mws.sh**: Get the open maintenance windows on the PagerDuty account. 
* **get_oncalls.sh**: Get the on call responders for a specific schedule. Pass the schedule ID on the command line. A comment also includes the url for selecting on call shifts by user ID.
* **get_resolved_incidents.sh**: Get the resolved incidents on a specific service for the past 30 days. Pass the service ID on the command line.
* **get_schedule.sh**: Get a single schedule. Pass the schedule ID on the command line. 
* **get_sched_since.sh**: Get the entries for a specific on call schedule over the last 30 days. Pass the schedule ID on the command line.
* **get_services.sh**: Get all the services on the account. Not paginated. Requires only `PD_API_KEY`.
* **get_userlog.sh**: Get the log entries for the requested user. Pass the user ID on the command line.
* **get_users.sh**: Get the users on a team. Pass the team ID on the command line. Requires only `PD_API_KEY`.
* **mass_resolve.sh**: Not sure this one works. Resolve multiple incidents in the same request. Add incident IDs *to the script*, not set up for arguments.
* **one_vendor.sh**: Get information about a single integration vendor. Pass the vendor ID on the command line.
* **resolve_incident.sh**: Resolve a specific incident. Pass the incident ID on the command line.
* 

### Python
Some python scripts for working with the API. These make use of the [pagerduty library](https://github.com/PagerDuty/python-pagerduty).

These use the same environment variables for authentication that the bash scripts use:
* `PD_API_KEY`: your PagerDuty [API Key](https://developer.pagerduty.com/docs/authentication)
* `PD_FROM_ADDR`: an email address associated with a PagerDuty user account. This will attribute any changes to that user.

**Scripts were mostly written against python 3.8 or 3.12.**

