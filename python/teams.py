import os
from pdpyras import APISession

users = ["PM82RFK", "PQWNAVE"]
team = 'PAKFPTY'

api_token = os.environ['PD_API_KEY']
session = APISession(api_token)

# teams = session.list_all(
#     'teams',
#     params={'id': team}
# )

# print(teams)
# url = "teams/{}/users/{}".format(team, users[0])
# print(url)
role = """
{
    "role": "observer"
}
"""

for u in users:
    url = "teams/{}/users/{}".format(team, u)
    print(url)
    output = session.rput(url, json=role, headers={"From": "mwalls@pagerduty.com"})
    print(output)
