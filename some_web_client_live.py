import requests


class SomeResourceClient:
    def __init__(self, url):
        self.url = url

    def user_get_status(self, user_id):
        resp = requests.get(f"{self.url}/web/user/get-status/{user_id}")
        c = 1


some_resource_client = SomeResourceClient("https://www.avito.ru")
some_resource_client.user_get_status(20405678)
