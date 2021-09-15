import pytest
import json
from truck_delivery_pamy.db_connector import DBConnector


def test_save_mock(mocker):
    mocker.patch("redis.Redis.set").return_value = True

    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    db_connector = DBConnector()
    result_save = db_connector.save(id_test, object_to_save)
    assert result_save == True


def test_get_by_id_mock(mocker):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    mocker.patch("redis.Redis.set").return_value = True
    mocker.patch("redis.Redis.get").return_value = json.dumps(object_to_save)

    db_connector = DBConnector()
    db_connector.save(id_test, object_to_save)

    result = db_connector.get_by_id(id_test)
    assert result == object_to_save


