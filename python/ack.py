"""
  Acknowledge and incident
"""

import sys
import os
from pagerduty import RestApiV2Client, EventsAPIV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']
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


