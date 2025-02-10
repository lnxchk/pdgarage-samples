#!/usr/bin/env python3
"""
Walk the service graph of a particular PagerDuty business service.

Pass the service ID on the command line or enter it at the prompt.
"""

import os
import sys
import requests

# auth
# find the api tokens in your account /api-keys
# to create a new key, you'll need to be a "manager" or "owner"
api_token = os.environ['PD_API_KEY']
indent_level = 0
names_dict = {}

def print_indent():
    print("  " * indent_level, end="")


def make_req(endpoint):
    url = "https://api.pagerduty.com/{}".format(endpoint)
    headers = {"Accept": "application/vnd.pagerduty+json;version=2",
           "Authorization": "Token token={}".format(api_token),
           "Content-Type": "application/json"}
    return requests.get(url, headers=headers)


def get_biz_deps(serv_id):
    global indent_level
    # print("in get_biz_deps with id {}".format(id))
    if serv_id in names_dict.keys():
        my_name = names_dict[serv_id]
    else:
        my_name = get_biz_serv_name(serv_id)
    print_indent()
    print("{} (Business Service)".format(my_name))
    indent_level += 1
    endpoint = "service_dependencies/business_services/{}".format(serv_id)
    my_deps = make_req(endpoint)
    data = my_deps.json()
    for relation in data['relationships']:
        if relation['supporting_service']['id'] == serv_id:
            continue
        if relation['supporting_service']['type'] == "business_service_reference":
            get_biz_deps(relation['supporting_service']['id'])
        elif relation['supporting_service']['type'] == "technical_service_reference":
            get_tech_deps(relation['supporting_service']['id'])
    indent_level -= 1


def get_tech_deps(serv_id):
    global indent_level
    if serv_id in names_dict.keys():
        my_name = names_dict[serv_id]
    else:
        my_name = get_tech_serv_name(serv_id)
    print_indent()
    print("{} (Technical Service)".format(my_name))
    indent_level += 1
    endpoint = "service_dependencies/technical_services/{}".format(serv_id)
    my_deps = make_req(endpoint)
    data = my_deps.json()
    for relation in data['relationships']:
        if relation['supporting_service']['id'] == serv_id:
            continue
        if relation['supporting_service']['type'] == "business_service_reference":
            get_biz_deps(relation['supporting_service']['id'])
        elif relation['supporting_service']['type'] == "technical_service_reference":
            get_tech_deps(relation['supporting_service']['id'])
    indent_level -= 1


def get_tech_serv_name(id):
    endpoint = "services/{}".format(id)
    this_service_resp = make_req(endpoint)
    this_service = this_service_resp.json()
    names_dict[id] = this_service['service']['name']
    return(this_service['service']['name'])


def get_biz_serv_name(id):
    endpoint = "business_services/{}".format(id)
    this_service_resp = make_req(endpoint)
    this_service = this_service_resp.json()
    names_dict[id] = this_service['business_service']['name']
    return(this_service['business_service']['name'])


if __name__ == '__main__':
    # you can pass the service ID on the command line or enter it at the prompt
    if len(sys.argv) < 2:
        this_service = input("Which business service? ")
    else:
        this_service = str(sys.argv[1])

    get_biz_deps(this_service)
