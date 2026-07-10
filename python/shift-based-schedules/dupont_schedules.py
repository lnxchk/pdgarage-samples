"""
Shift-Based Schedules

Custom schedules example for the new Schedules v3 API

"""

import sys
import os
import requests
import json
from datetime import datetime, timedelta

# setting up for the v3 endpoint
host = "https://api.pagerduty.com/v3"

# set up other required headers 
# will change this when the python library is updated
api_token = os.environ['PD_API_KEY']
from_addr = os.environ['PD_FROM_ADDR']
headers = {"Accept": "application/json",
           "Authorization": "Token token={}".format(api_token),
           "Content-Type": "application/json",
           }

print(headers)
#sys.exit()
"""

Create a new schedule

{
  "schedule": {
    "name": "Engineering On-Call",
    "time_zone": "America/New_York"
  }
}

"""
url = "https://api.pagerduty.com/v3/schedules"
#data = {
#    'schedule': {
#        'name': 'Testing Schedule 2',
#        'time_zone': 'America/New_York'
#    }
#}
#print(data)
#j_data = json.dumps(data)
#response = requests.post(url, headers=headers, json=data)

#response.raise_for_status()
#data = response.json()
#print(f"Schedule ID is {data["schedule"]["id"]}")

#sched_id = data["schedule"]["id"]


# now make shifts into this schedule

class DupontShift:
    # Dupont shifts are 12 hours. We'll configure those 12 hours somewhere and 
    # then these classes only need to know "day" or "night"
    # include the scedule ID and the User ID for the shift
    day_start = "09:00:00"
    night_start = "21:00:00"
    def __init__(self, user, shift_date, day_part):
        self.user = user
        self.shift_date = shift_date
        self.day_part = day_part

    def buildShift(self):
        if self.day_part == "day":
            shift_start = self.day_start
            shift_end = self.night_start
            end_date = self.shift_date
        elif self.day_part == "night":
            shift_start = self.night_start
            shift_end = self.day_start
            parsed_date = datetime.strptime(self.shift_date, "%Y-%m-%d")
            end_date = (parsed_date + timedelta(days = 1)).strftime("%Y-%m-%d")

        start_time = f"{self.shift_date}T{shift_start}-04:00"
        end_time = f"{end_date}T{shift_end}-04:00"
        return custom_shift(self.user, start_time, end_time)



def custom_shift(user, start_time, end_time):
    ## schedule_id goes in the url of the call, not in the payload
    json_data = {
      "type": "custom_shift",
      "start_time": start_time,
      "end_time": end_time,
      "assignments": [
        {
          "type": "shift_assignment",
          "member": {
            "type": "user_member",
            "user_id": user
            }
        }
      ]
    }
    return json_data


schedule_id = "PD***4J"
team1 = ["PC***C9"]
team2 = ["PU***NW"]
team3 = ["P7***6T"]
team4 = ["P1***MQ"]

# build weeks
# week 1:
week1 = ["night", "night", "night", "night", "off", "off", "off"]
# week 2:
week2 = ["day", "day", "day", "off", "night", "night", "night"]
# week 3:
week3 = ["off", "off", "off", "day", "day", "day", "day"]
# week 4:
week4 = ["off", "off", "off", "off", "off", "off", "off"]

month_start = "2026-08-31"
json_shifts = {
    "custom_shifts": []
}

# team1 runs week1, week2, week3, week4
# team 1:
for member in team1:
    date = month_start
    for day_part in week1 + week2 + week3 + week4:
      if day_part != "off":
        shift = DupontShift(member, date, day_part)
        #print(shift.buildShift())
        json_shifts["custom_shifts"].append(shift.buildShift())
      # increment the date
      parsed_date = datetime.strptime(date, "%Y-%m-%d")
      date = (parsed_date + timedelta(days = 1)).strftime("%Y-%m-%d")

# team2 runs week2, week3, week4, week1
for member in team2:
    date = month_start
    for day_part in week2 + week3 + week4 + week1:
        if day_part != "off":
            shift = DupontShift(member, date, day_part)
            #print(shift.buildShift())
            json_shifts["custom_shifts"].append(shift.buildShift())
            #shifts += shift.buildShift()
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
        date = (parsed_date + timedelta(days = +1)).strftime("%Y-%m-%d")

# team3 runs week3, week4, week1, week2
for member in team3:
    date = month_start
    for day_part in week3 + week4 + week1 + week2:
        if day_part != "off":
            shift = DupontShift(member, date, day_part)
            json_shifts["custom_shifts"].append(shift.buildShift())
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
        date = (parsed_date + timedelta(days = +1)).strftime("%Y-%m-%d")

# team4 runs week4, week1, week2, week3
for member in team4:
    date = month_start
    for day_part in week4 + week1 + week2 + week3:
        if day_part != "off":
            shift = DupontShift(member, date, day_part)
            json_shifts["custom_shifts"].append(shift.buildShift())
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
        date = (parsed_date + timedelta(days = +1)).strftime("%Y-%m-%d")

#final_json = json.dumps(json_shifts, indent=2)
#print(final_json)

# make the API call
endpoint = f"{url}/{schedule_id}/custom_shifts"
response = requests.post(endpoint, headers=headers, json=json_shifts)
print(response.text)
