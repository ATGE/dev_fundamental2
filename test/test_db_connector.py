
import pytest

def test_save():
    id_test = "123"
    object_to_save = {"123": {"a":"a"}}

    db_connector = DbConnector()
    db_connector.save(id_test, object_to_save)


def test_get_by_id():
    id_test = "123"
    object_to_save = {"123": {"a":"a"}}

    db_connector = DbConnector()
    db_connector.save(id_save, object_to_save)

    result = db_connector.get_by_id(id_test)
    assert result == object_to_save
