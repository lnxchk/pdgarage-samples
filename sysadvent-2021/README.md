## Sample code for SysAdvent Post 2021
### Introduction to the PagerDuty API

- **code1.sh** - sample script to create an incident on a service in PagerDuty.
  - Requires: a working API Token for you account, a valid email address associated with your PagerDuty account, and a service ID.


- **code2.sh** - sample script to create an event in PagerDuty
  - Requires: a routing key assigned to a particular service, found in the integrations tab of that service.


- **code3.sh** - sample script to create a change event in PagerDuty
  - Requires: a routing key assigned to a particular service, found in the integrations tab of that service.


- **code4.sh** - a sample script to create a note on an existing incident currently active in your PagerDuty account.
  - Requires: the ID of an active incident, an API Token associated with your account, and a valid email address associated with your PagerDuty Account.


For more information on the PagerDuty API, please see the documentation at [https://developer.pagerduty.com/api-reference/](https://developer.pagerduty.com/api-reference/)
