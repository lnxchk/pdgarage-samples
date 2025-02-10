#!/usr/bin/env python3
"""
Escalation Policy Audit

Figure out if a team doesn't have an escalation policy

Teams and escalation policies don't have a 1:1 relationship, 
and escalation policies are not attached to or noted in the 
team object. We can brute force it:

1. Query for teams
2. Build a list of those teams, include useful data
3. Query escalation policies
4. Check which teams are included in escalation policies

escalation policies: https://developer.pagerduty.com/api-reference/51b21014a4f5a-list-escalation-policies
teams: https://developer.pagerduty.com/api-reference/0138639504311-list-teams
"""

import os
from pagerduty import RestApiV2Client

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']

# initialize the session
session = RestApiV2Client(api_token)
teams_dict = {}


def get_teams():
    # get all the teams in the account, add team ids to the dictionary
    # picking html_url as the value, but if 'summary' or something else
    # is more helpful, use that
    endpoint = "/teams"
    teams_resp = session.list_all(endpoint)
    for team in teams_resp:
        teams_dict[team['id']] = team['html_url']


def get_eps():
    # get the escalation policies
    # read each team from the escalation policy:
    #   teams are an array subkey in the escalation policy object
    # for each included team, tick the value in the dictionary
    endpoint = "/escalation_policies"
    eps_resp = session.list_all(endpoint)
    for ep in eps_resp:
        for team in ep['teams']:
            eps_dict[team['id']] += 1



if __name__ == '__main__':
    get_teams()
    # use the teams to create a new dictionary to track escalation policies
    eps_dict = dict.fromkeys(teams_dict.keys(), 0)
    get_eps()

    for team in teams_dict.keys():
        if eps_dict[team] == 0:
            print("team {} does not have an ep".format(teams_dict[team]))
