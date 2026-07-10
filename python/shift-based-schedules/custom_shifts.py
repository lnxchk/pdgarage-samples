"""
custom_shifts.py

some helper functions for creating custom shifts using shift-based schedules

"""
import csv

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

def shifts_from_csv(filename):
    print(f"Reading shifts from {filename}")
    shift_data = {
        "custom_shifts": []
    }
    with open(filename, "r") as file:
        file_data = csv.DictReader(file)
        for shift in file_data:
            # user_id, start_date (YYYY-MM-DD), start_time (HH:MM:SS), end_date, end_time
            shift_data["custom_shifts"].append(custom_shift(shift["UserID"], shift["StartTime"], shift["EndTime"]))

    return shift_data