import socket
import requests
import os
import json
from contextlib import closing


api_token = os.environ['PD_API_KEY']
from_addr = os.environ['PD_FROM_ADDR']

SERVICE_ID = "PLOSNGW"


def check_socket(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            return True
        else:
            return False


def send_pd_event(service_name):
    # set up a POST request for PD API
    headers = {"Accept": "application/vnd.pagerduty+json;version=2",
               "Authorization": "Token token={}".format(api_token),
               "Content-Type": "application/json",
               "From": "{}".format(from_addr)}
    data = {
        "incident": {
            "type": "incident",
            "title": "The service {} is not running".format(service_name),
            "service": {
                "id": SERVICE_ID,
                "summary": "null",
                "type": "service_reference",
                "self": "null",
                "html_url": "null"
            }
        }
    }
    j_data = json.dumps(data)
    url = "https://api.pagerduty.com/incidents"
    my_incident = requests.post(url, headers=headers, data=j_data)
    my_incident.raise_for_status()
    print(my_incident.text)


if not check_socket("0.0.0.0", 80):
    send_pd_event("nginx")
else:
    print("nginx is ok")
