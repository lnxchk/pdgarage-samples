# Sample scripts for accessing parts of the PagerDuty API
Many of these pieces were inspired by questions in our [Community Forums](https://community.pagerduty.com)

None of these are *guaranteed* to work. Many of them do; they are intended as examples, not solutions.

## Sample files in this project:

### Bash
Unless otherwise specified, these scripts require two environment variables:
* `PD_API_KEY`: your PagerDuty [API Key](https://developer.pagerduty.com/docs/authentication). Since these scripts touch a lot of different objects, they use a generic global key.
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
* **get_service_ep.sh**: Get a service, and include the escalation policies associated with that service. Pass the service ID on the command line.
* **get_userlog.sh**: Get the log entries for the requested user. Pass the user ID on the command line.
* **get_users.sh**: Get the users on a team. Pass the team ID on the command line. Requires only `PD_API_KEY`.
* **mass_resolve.sh**: Not sure this one works. Resolve multiple incidents in the same request. Add incident IDs *to the script*, not set up for arguments.
* **one_vendor.sh**: Get information about a single integration vendor. Pass the vendor ID on the command line.
* **resolve_incident.sh**: Resolve a specific incident. Pass the incident ID on the command line.


### Python
Some python scripts for working with the API. These make use of the [pagerduty library](https://github.com/PagerDuty/python-pagerduty).

These use the same environment variables for authentication that the bash scripts use:
* `PD_API_KEY`: your PagerDuty [API Key](https://developer.pagerduty.com/docs/authentication). Like the bash scripts, these touch a lot of different objects, so use a generic global API key.
* `PD_FROM_ADDR`: an email address associated with a PagerDuty user account. This will attribute any changes to that user.

**Scripts were mostly written against python 3.8 or 3.12.**

* **ack_and_assign.py**: Acknowledge an incident and add a responder. Pass the incident ID and user ID of the responder on the command line
* **ack.py**: Basic acknowledge. Pass the incident ID on the command line
* **all_log_entries.py**: Get the log entries. The log records incident events across the entire account. Example not paginated, but endpoint provides pagination.
* **all_service_deps.py**: Get the immediate service dependencies of a service. Requests service ID as input. Does not traverse the dependency tree.
* **all_service_integrations.py**: Get all the services in an account, include the information about their integrations. Print out the service name, service ID, and select information about each integration.
* **analytics_query.py**: Request incident data from the analytics endpoint. Requests a team ID from input or command line. Example query options for urgency and time window. 
* **audit_schedule.py**: Show the record of changes that have been made to a schedule. Pass the schedule ID on the command line or input it at the prompt
* **bump_incidents_high_urgency.py**: Bump all triggered incidents on a given service to high urgency. This can trigger new workflows and other functions depending on your setup. Pass the service ID on the command line or input it at the prompt.
* **create_and_assign.py**: Create an incident and assign a responder. Pass the service ID and the responder's user ID on the command line
* **create_bizserv_deps.py**: Create a dependency relationship between two business services, as an example. Enter the service IDs at the prompts.
* **create_mws.py**: Create maintenance windows. This prompts for the needed info and builds the timestamps.
* **create_service_deps.py**: Similar to `create_bizserv_deps.py`, creates a dependency relationship between two services. This script allows a technical service to be a dependency of a business service. Enter the service IDs at the prompts.
* **custom_fields_incident.py**: Fetch the custom fields included in a specific incident. Pass the incident ID on the command line or enter it at the prompt. Command line is better if planning to use an output parser like `jq`.
* **ep_audit.py**: From a forums question. Query the API for teams in your PagerDuty account, and then determine which teams do not have an escalation policy. Escalation Policies and teams don't necessarily have a relationship, and there is no requirement for a team to have an EP. 
* **event_orch_delete.py**: Another from a forums question. This one queries the API for all Event Orchestrations on the account, presents the rules to the first EO to the user, and prompts for a rule to delete. Could use some work to account for many EOs on an account.
* **event_sample.py**: Send a basic event to the events API. Requires a routing key stored in the `PD_ROUTE_KEY` environment variable.
* **find_dependent_services.py**: Walk the service graph of a particular PagerDuty business service. Pass the service ID on the command line or enter it at the prompt.
* **full_service.py**: Service query including example parameters and output parsing. Pass the service ID on the command line or enter it at the prompt.
* **get_alerts_and_notes.py**: Finding the notes and alerts attached to a service that meets a specific requirement. Basic example, could be honed to specific teams, services, etc.
* **get_alerts_incident.py**: Get all of the incidents associated with a specific incident. Pass the incident ID on the command line or enter it at the prompt. Returns JSON of the alerts.
* **get_all_incidents.py**: Get all incidents, with example parameters. Includes basic pagination.
* **get_all_oncalls.py**: Get all of the on call responders in a PagerDuty account. Doesn't de-dupe the escalation policies in the case that multiple responders are oncall.
* **get_all_users_token.py**: Get all of the users on an account using a user token, rather than a global API key.
* **get_all_users.py**: Get all the users on an account. Uses the global `PD_API_KEY`. Outputs JSON.
* **get_deleted_user.py**: Forum question. Looking for a deleted user in an on call schedule. Queries for all schedules in the account. Prints out a specific message, not account object data. Deleted users show up in historical and analytics data about the schedule.
* **get_escpol.py**: Get an escalation policy. Enter the ID on the command line or at the prompt.
* **get_incident.py**: Basic incident retrieval. Pass the incident ID on the command line or enter it at the prompt.
* **get_incidents_b.py**: Sample showing more advanced options to query the `/incidents` endpoint.
* **get_mws.py**: Get maintenance window IDs. Building block for other code.
* **get_no_oncalls.py**: Find users who have no oncall assignments. Similar queries can be used to show all oncall shifts for a given user.
* **get_oncall_for_sched.py**: Get all responders included in a schedule. Pass the schedule ID on the command line or enter it at the prompt. Includes a couple of query options, depending on what you want to see.
* **get_oncalls.py**: sets up some example queries for the `/oncalls` endpoint, including using `since` and `until`.
* **get_one_user.py**: Gets all the info about one user. Pass the user ID on the command line or enter it at the prompt.
* **get_outlier_list.py**: Use the `/incidents/{}/outlier_incident` endpoint to get outlier info about all `triggered` and `acknowledged` incidents. Returns the incident ID and it's category i.e. `rare` or `novel`, etc
* **get_sched.py**: Get the next four weeks of an on call schedule. Pass the schedule ID on the command line or enter it at the prompt.
* **get_services.py**: Basic query of the `/services` endpoint.
* **get_some_users.py**: Example of the `/users` endpoint, using an iterator and the `query` option. Enter the name to query on the command line or at the prompt.
* **get_team_eps.py**: Retrieve the escalation policies associated with a specific team. Pass the team ID on the command line or enter it at the prompt.
* **get_team.py**: Query the `/teams/` endpoint for info about a single team. Pass the team ID on the command line or enter it at the prompt.
* **incidents_all_the_things.py**: Very silly. Queries `/incidents` endpoint and displays all of the `include[]` parameters. *Will produce a lot of data for your incidents.* Best if used on a single incident at a time.
* **incidents_by_team.py**: *TODO update for new `datetime` objects.* This was a forums question, to find the number of incidents associated with a specific team during a selected time period. Pass the team ID on the command line or enter it at the prompt. 
* **incidents_since.py**: *TODO update for new `datetime` objects.* Query the `/incidents/` endpoint for incidents on a specific service using `since` and `until` parameters. Pass the service on the command line or enter it at the prompt. Hardcoded to 10 days.
* **