import pytest
import responses

from some_web_client_live import SomeResourceClient


def test_some_web_client():
    valid_json_answer = {
        "lastActionTime": 1672113865,
        "timeDiff": 23963
    }

    responses.add(responses.GET, "https://www.avito.ru/web/2/user/get-status/7e59e245162b490c6ea0edf90dbedc74996db8b9122eda86e45011228299bff6",
                  json=valid_json_answer, status=200)

    some_resource_client = SomeResourceClient("https://www.avito.ru")
    res = some_resource_client.get_user_last_action_time("7e59e245162b490c6ea0edf90dbedc74996db8b9122eda86e45011228299bff6")
    c = 1


    #mock создание некой заглушки, функция которая возвращает заранее заготовленный результат
