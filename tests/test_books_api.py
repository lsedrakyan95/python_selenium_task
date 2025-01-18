import pytest
from assertpy import assert_that
from api.book_api import BookAPI
from tests.data.book_data import get_book_data

def setup_module(module):
    print('\nStart running tests of Books API...\n')

def teardown_module(module):
    print('\nFinish running tests of Books API...\n')

@pytest.fixture(scope="module")
def api_client():
    """Fixture to provide an instance of BookAPI for testing."""
    return BookAPI()

def test_get_latest_books_with_empty_list(api_client):
    response = api_client.get_latest_books(limit=1)
    assert_that(response.status_code).is_equal_to(404)
    assert_that(response.json()["message"]).is_equal_to('There is no such book | books.')

def test_get_latest_books_value(api_client):
    book_data: dict[str, str] = get_book_data()
    response_book = api_client.post_book_manipulation(book_data)
    response = api_client.get_latest_books(limit=1)
    assert_that(response.status_code).is_equal_to(200)

    item = response.json()[0]
    assert_that(item['type']).is_equal_to(book_data['type'])
    assert_that(item['title']).is_equal_to(book_data['title'])
    assert_that(item['creation_date']).is_equal_to(book_data['creation_date'])
    assert_that(item['id']).is_equal_to(response_book.json()['id'])
    assert_that(item['updated_date_time']).is_equal_to(response_book.json()['updated_date_time'])

def test_get_latest_books_schema(api_client):
    response = api_client.get_latest_books(limit=1)
    assert_that(len(response.json())).is_equal_to(1)
    assert_that(response.json()).is_instance_of(list)

    item = response.json()[0]
    assert_that(item).is_instance_of(dict)
    assert_that(item['type']).is_type_of(str)
    assert_that(item['title']).is_type_of(str)
    assert_that(item['id']).is_type_of(str)
    assert_that(item['id']).matches(r'^[0-9a-fA-F-]{36}$')
    assert_that(item['creation_date']).is_type_of(str)
    assert_that(item['updated_date_time']).is_type_of(str)

def test_get_latest_books_limit(api_client):
    api_client.post_book_manipulation(get_book_data())
    api_client.post_book_manipulation(get_book_data())
    response = api_client.get_latest_books(limit=2)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(len(response.json())).is_equal_to(2)

def test_post_book_manipulation_schema(api_client):
    book_data = get_book_data()
    response = api_client.post_book_manipulation(book_data)    
    item = response.json()
    assert_that(item).is_instance_of(dict)
    assert_that(item['type']).is_type_of(str)
    assert_that(item['title']).is_type_of(str)
    assert_that(item['id']).is_type_of(str)
    assert_that(item['id']).matches(r'^[0-9a-fA-F-]{36}$')
    assert_that(item['creation_date']).is_type_of(str)
    assert_that(item['updated_date_time']).is_type_of(str)

def test_post_book_manipulation_value(api_client):
    book_data = get_book_data()
    response = api_client.post_book_manipulation(book_data)
    assert_that(response.status_code).is_equal_to(200)

    item = response.json()
    assert_that(item['type']).is_equal_to(book_data['type'])
    assert_that(item['title']).is_equal_to(book_data['title'])
    assert_that(item['creation_date']).is_equal_to(book_data['creation_date'])

def test_post_book_manipulation_title(api_client):
    book_data = get_book_data()
    del book_data['title']
    response = api_client.post_book_manipulation(book_data)
    assert_that(response.status_code).is_equal_to(400)
    assert_that(response.json()["message"]).is_equal_to('The request is not valid.')

def test_post_book_manipulation_type(api_client):
    book_data = get_book_data()
    del book_data['type']
    response = api_client.post_book_manipulation(book_data)
    assert_that(response.status_code).is_equal_to(400)
    assert_that(response.json()["message"]).is_equal_to('The request is not valid.')

def test_post_book_manipulation_creation_date(api_client):
    book_data = get_book_data()
    del book_data['creation_date']
    response = api_client.post_book_manipulation(book_data)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()["creation_date"]).is_equal_to(None)

def test_get_book_info_with_wrong_id(api_client):
    book_id = '612daad5-92dc-4c07-966b-48b8008261e0'
    response = api_client.get_book_info(book_id)
    assert_that(response.status_code).is_equal_to(404)
    assert_that(response.json()["message"]).is_equal_to('There is no such book | books.')

def test_get_book_info_schema(api_client):
    book_data = get_book_data()
    response_book = api_client.post_book_manipulation(book_data)
    book_id = response_book.json()['id']
    response = api_client.get_book_info(book_id)
    item = response.json()
    assert_that(item).is_instance_of(dict)
    assert_that(item['type']).is_type_of(str)
    assert_that(item['title']).is_type_of(str)
    assert_that(item['id']).is_type_of(str)
    assert_that(item['id']).matches(r'^[0-9a-fA-F-]{36}$')
    assert_that(item['creation_date']).is_type_of(str)
    assert_that(item['updated_date_time']).is_type_of(str)

def test_get_book_info_value(api_client):
    book_data = get_book_data()
    response_book = api_client.post_book_manipulation(book_data)
    book_id = response_book.json()['id']
    response = api_client.get_book_info(book_id)
    assert_that(response.status_code).is_equal_to(200)

    item = response.json()
    assert_that(item['type']).is_equal_to(book_data['type'])
    assert_that(item['title']).is_equal_to(book_data['title'])
    assert_that(item['creation_date']).is_equal_to(book_data['creation_date'])
    assert_that(item['id']).is_equal_to(response_book.json()['id'])
    assert_that(item['updated_date_time']).is_equal_to(response_book.json()['updated_date_time'])