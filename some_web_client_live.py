import requests
import json
from datetime import datetime


class SomeResourceClient:
    def __init__(self, url):
        self.url = url

    def __user_get_status(self, user_id):
        resp = requests.get(f"{self.url}/clickstream/events/1/{user_id}")
        json_data = json.loads(resp.text)
        return json_data

    def get_user_last_action_time(self, user_id):
        json_data = self.user_get_status(user_id)
        last_action_time = json_data["result"]
        time_diff = json_data["timeDiff"]
        return datetime.fromtimestamp(last_action_time - time_diff)


some_resource_client = SomeResourceClient("https://cs.avito.ru")
some_resource_client.user_get_status("json")
