import pytest


@pytest.fixture
def db_connector():
    db_conn = Dbconnector()
    db_conn.open()
    yield db_conn
    db_conn.close()