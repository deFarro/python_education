import requests
import sys


def get_token():
    if len(sys.argv) < 2:
        with open('.token.txt') as file:
            return file.read()
    else:
        return sys.argv[1]


TOKEN = get_token()
COUNTER_ID = '47559376'

request_link = 'https://api-metrika.yandex.ru/stat/v1/data?'


class YaMeCounter:
    def __init__(self, counter_id, token):
        self.headers = {
            "Authorization": "OAuth {}".format(token.rstrip()),
            "Content-Type": "application-json"
        }
        self.params = {
            "id": counter_id
        }

    @property
    def get_visits(self):
        temp_params = self.params
        temp_params["metrics"] = "ym:s:visits"
        res = requests.get(request_link, params=temp_params, headers=self.headers)
        return res.json()["totals"][0]

    @property
    def get_pageviews(self):
        temp_params = self.params
        temp_params["metrics"] = "ym:pv:pageviews"
        res = requests.get(request_link, params=temp_params, headers=self.headers)
        return res.json()["totals"][0]

    @property
    def get_users(self):
        temp_params = self.params
        temp_params["metrics"] = "ym:up:users"
        res = requests.get(request_link, params=temp_params, headers=self.headers)
        return res.json()["totals"][0]


counter = YaMeCounter(COUNTER_ID, TOKEN)

print(counter.get_visits)
print(counter.get_pageviews)
print(counter.get_users)
