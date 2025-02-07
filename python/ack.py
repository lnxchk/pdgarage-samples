<<<<<<< HEAD
#!/usr/bin/env python3
"""
  Acknowledge an incident
  Pass the incident ID on the command line

=======
"""
  Acknowledge and incident
>>>>>>> 68b2cb9e09cf23ea25b561a290b39628cf1aab5f
"""

import sys
import os
<<<<<<< HEAD
from pagerduty import RestApiV2Client
=======
from pagerduty import RestApiV2Client, EventsAPIV2Client
>>>>>>> 68b2cb9e09cf23ea25b561a290b39628cf1aab5f

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']
<<<<<<< HEAD
from_addr = os.environ['PD_FROM_ADDR']

incident = sys.argv[1]

# initialize the session
session = RestApiV2Client(api_token, default_from=from_addr)

my_incident = session.rget(f"/incidents/{incident}")
my_incident['status'] = "acknowledged"
updated_incident = session.rput(f"/incidents/{incident}", json=my_incident)
=======
routing_key = os.environ['PD_ROUTE_KEY']

# initialize the session
session = RestApiV2Client(api_token, default_from="mwalls+abby@pagerduty.com")
# event_session = EventsAPIV2Client(routing_key)

# dedup_key = event_session.trigger("Server is on fire", 'dusty.old.server.net')
# event_session.acknowledge(dedup_key)
# event_session.resolve(dedup_key)

my_incident = session.rget('/incidents/Q2P0OU7QZHLD48')
my_incident['status'] = "acknowledged"
updated_incident = session.rput('/incidents/Q2P0OU7QZHLD48', json=my_incident)
>>>>>>> 68b2cb9e09cf23ea25b561a290b39628cf1aab5f


