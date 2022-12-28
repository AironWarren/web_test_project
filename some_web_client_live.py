import requests
import json
from datetime import datetime


class SomeResourceClient:
    def __init__(self, url):
        self.url = url

    def user_get_status(self, user_id):
        resp = requests.get(f"{self.url}/web/2/user/get-status/{user_id}")
        json_data = json.loads(resp.text)
        return json_data

    def get_user_last_action_time(self, user_id):
        json_data = self.user_get_status(user_id)
        last_action_time = json_data["lastActionTime"]
        time_diff = json_data["timeDiff"]
        return datetime.fromtimestamp(last_action_time - time_diff)


if __name__ == "__main__":
    some_resource_client = SomeResourceClient("https://www.avito.ru")
    print(some_resource_client.user_get_status("7e59e245162b490c6ea0edf90dbedc74996db8b9122eda86e45011228299bff6"))
    print(some_resource_client.get_user_last_action_time("7e59e245162b490c6ea0edf90dbedc74996db8b9122eda86e45011228299bff6"))
