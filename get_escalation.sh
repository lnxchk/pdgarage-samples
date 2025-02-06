#!/usr/bin/env bash
# ************
# 
# show an escalation policy. 
#
# usage: ./get_escalation.sh <ESCALATION POLICY ID>
#
# if you have a javascript parser like jq, you 
# can pipe the output of this script to it
#
# ************

# Your token. This is an Account-level credential
# https://youraccount.pagerduty.com/api_keys
TOKEN=$PD_API_KEY
EP=$1

ENDPOINT="https://api.pagerduty.com/escalation_policies/$EP"

curl -X GET --header 'Content-Type: application/json' \
--url $ENDPOINT \
--header 'Accept: application/vnd.pagerduty+json;version=2' \
--header "Authorization: Token token=$TOKEN" 
echo
