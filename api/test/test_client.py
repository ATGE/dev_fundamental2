import json
import pytest

from api.__main__ import app


def test_main_exception():
    with app.test_client() as client:
        rv = client.get('/')

    assert b'Index Page' == rv.data


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_main_index(client):
    rv = client.get('/')

    assert b'Index Page' == rv.data

    assert 200 == rv.status_code


@pytest.mark.parametrize('book_id,code',
                         [(2, 200),
                          (1, 200),
                          (0, 200),
                          (9, 500)
                          ])
def test_books_by_id(client, book_id, code):
    rv = client.get(f'/books/{book_id}')
    assert isinstance(rv.json, dict)
    assert code == rv.status_code
    assert rv.json.get("id") == book_id


def test_save_book(client):
    rv = client.post('/books',

                     headers={"Content-Type": "application/json"},

                     json=json.dumps({'id': 3,

                                      'title': 'Testing',

                                      'author': 'Testing',

                                      'first_sentence': 'to wound the autumnal city.',

                                      'published': '1975'}))

    assert rv.status_code == 200

    rv = client.get('/books/3')

    assert 200 == rv.status_code

    assert isinstance(rv.json, dict)

    assert rv.json.get("id") == 3
