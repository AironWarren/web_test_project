import pytest
import responses
from some_web_client_live import SomeResourceClient
from datetime import datetime


@responses.activate
def test_some_web_client():
    # позитивный кейс,то что должна отдавать ручка, json подобная структура
    valid_json_answer = {
        "lastActionTime": 1672113865,
        "timeDiff": 23963
    }

    # mock создание некой заглушки, функция которая возвращает заранее заготовленный результат
    responses.add(method=responses.GET,
                  url="https://www.avito.ru/web/2/user/get-status/7e59e245162b490c6ea0edf90dbedc74996db8b9122eda86e45011228299bff6",
                  json=valid_json_answer, status=200)

    some_resource_client = SomeResourceClient("https://www.avito.ru")
    res = some_resource_client.get_user_last_action_time(
        "7e59e245162b490c6ea0edf90dbedc74996db8b9122eda86e45011228299bff6")
    assert res == datetime.fromtimestamp(valid_json_answer["lastActionTime"] - valid_json_answer["timeDiff"])


@responses.activate
def test_some_web_client_with_error():
    # позитивный кейс,то что должна отдавать ручка, json подобная структура
    valid_json_answer_with_error = {
        "errors": [
            "Not found"]
    }

    # mock создание некой заглушки, функция которая возвращает заранее заготовленный результат
    responses.add(method=responses.GET,
                  url="https://www.avito.ru/web/2/user/get-status/7e59e245162b490c6ea0edf90dbedc74996db8b9122eda86e45011228299bff6-",
                  json=valid_json_answer_with_error, status=404)

    with pytest.raises(KeyError):
        some_resource_client = SomeResourceClient("https://www.avito.ru")
        some_resource_client.get_user_last_action_time(
            "7e59e245162b490c6ea0edf90dbedc74996db8b9122eda86e45011228299bff6-")
