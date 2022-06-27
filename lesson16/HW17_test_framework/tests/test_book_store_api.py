import pytest
from lesson16.HW17_test_framework.api_collections.bookstore import BookstoreAPI
from lesson16.HW17_test_framework.api_collections.login import LoginAPI
from http import HTTPStatus
from lesson16.HW17_test_framework.api_collections.logout import LogoutAPI
from lesson16.HW17_test_framework.api_collections.user import UserAPI
import json


@pytest.mark.positive
def test_get_login_page():
    """
     Description: test checks GET method for user login page

     Pre-conditions:
     None

     Steps:
     1. Send GET request for login page
     2. Check status code and response reason

     Expected:
     1. After sending GET request we receive HTTPStatus.OK and response reason as 'OK'
     """
    login_page_response = LoginAPI().get_login_page()
    assert login_page_response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\n' \
                                                             f'Actual: {login_page_response.status_code}' \
                                                             f'\nExpected: {HTTPStatus.OK}'
    assert login_page_response.reason == 'OK'

@pytest.mark.positive
def test_post_login_page():
    """
     Description: test checks POST method for user login page

     Pre-conditions:
     None

     Steps:
     1. Send POST request for login page with user login and password
     2. Check status code and response reason

     Post-conditions:
     Logout from the system

     Expected:
     1. After sending POST request we receive HTTPStatus.OK and response reason as 'OK'
     """
    login_page_post_response = LoginAPI().post_login_user()
    assert login_page_post_response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\n' \
                                                                  f'Actual: {login_page_post_response.status_code}' \
                                                                  f'\nExpected: {HTTPStatus.OK}'
    assert login_page_post_response.reason == 'OK'
    #post-cond
    LogoutAPI().get_logout_page()

@pytest.mark.positive
def test_get_logout_page():
    """
     Description: test checks GET method for user logout page

     Pre-conditions:
     1. Send POST request for login page with user login and password

     Steps:
     1. Send GET request for logout page
     2. Check status code and response reason

     Post-conditions:
     None

     Expected:
     1. After sending GET request we receive HTTPStatus.OK and response reason as 'OK'
     """
    # pre-cond
    LoginAPI().post_login_user()
    #test
    logout_page_response = LogoutAPI().get_logout_page()
    assert logout_page_response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\n' \
                                                             f'Actual: {logout_page_response.status_code}' \
                                                             f'\nExpected: {HTTPStatus.OK}'
    assert logout_page_response.reason == 'OK'

@pytest.mark.positive
def test_add_book_for_user():
    """
     Description: test checks POST method for book store page in order to add book
     into user's collection
    
     Pre-conditions:
     1. Send POST request for login page with user login and password
     2. Extract user id and token from server response

     Steps:
     1. Send POST request to add a single book for user
     2. Check status code and response reason

     Post-conditions:
     1. Delete book for user
     2. Logout from website

     Expected:
     1. After sending POST request to add a book in user's list
     we receive HTTPStatus.CREATED and response reason as 'Created'
     """
    # pre-conditions
    login_page_post_response = LoginAPI().post_login_user()
    user_id = json.loads(login_page_post_response.text)["userId"]
    user_token = json.loads(login_page_post_response.text)["token"]
    # test
    isbn_number_to_add = "9781593275846"
    bookstore_page_post_response = BookstoreAPI().post_book_for_user(isbn_number_to_add, user_id, user_token)
    assert bookstore_page_post_response.status_code == HTTPStatus.CREATED, f'\nStatus code is not as expected\n' \
                                                                           f'Actual: {bookstore_page_post_response.status_code}' \
                                                                           f'\nExpected: {HTTPStatus.CREATED}'
    assert bookstore_page_post_response.reason == 'Created'
    # post-cond
    BookstoreAPI().delete_book_for_user(user_id, user_token, isbn_number_to_add)
    LogoutAPI().get_logout_page()


@pytest.mark.positive
def test_add_books_for_user():
    """
     Description: test checks POST method for book store page in order to add books
     into user's collection

     Pre-conditions:
     1. Send POST request for login page with user login and password
     2. Extract user id and token from server response

     Steps:
     1. Send POST request to add two books for user
     2. Check status code and response reason

     Post-conditions:
     1. Delete book for user
     2. Logout from website

     Expected:
     1. After sending POST request to add books into user's list
     we receive HTTPStatus.CREATED and response reason as 'Created'
     """
    # pre-conditions
    login_page_post_response = LoginAPI().post_login_user()
    user_id = json.loads(login_page_post_response.text)["userId"]
    user_token = json.loads(login_page_post_response.text)["token"]
    # add book
    isbn_number_to_add_1 = "9781593275846"
    isbn_number_to_add_2 = "9781449337711"
    bookstore_page_post_response = BookstoreAPI().post_books_for_user(user_id, user_token,
                                                                      isbn_num_1=isbn_number_to_add_1,
                                                                      isbn_num_2=isbn_number_to_add_2)
    assert bookstore_page_post_response.status_code == HTTPStatus.CREATED, f'\nStatus code is not as expected\n' \
                                                                           f'Actual: {bookstore_page_post_response.status_code}' \
                                                                           f'\nExpected: {HTTPStatus.CREATED}'
    assert bookstore_page_post_response.reason == 'Created'
    # post-cond
    BookstoreAPI().delete_book_for_user(user_id, user_token, isbn_number_to_add_1)
    BookstoreAPI().delete_book_for_user(user_id, user_token, isbn_number_to_add_2)
    LogoutAPI().get_logout_page()


@pytest.mark.negative
def test_add_same_book_for_user():
    """
     Description: test checks inability to add the book already available in
     user's collection using POST method for book store page

     Pre-conditions:
     1. Send POST request for login page with user login and password
     2. Extract user id and token from server response

     Steps:
     1. Send POST request to add  book for user
     2. Send POST request again to add the same book for user
     2. Check status code and response reason

     Post-conditions:
     1. Delete book for user
     2. Logout from website

     Expected:
     1. After sending POST request to add books already existing in user's collection
     we receive HTTPStatus.BAD_REQUEST and response content contains reason 'ISBN already present'
     """
    # pre-conditions
    login_page_post_response = LoginAPI().post_login_user()
    user_id = json.loads(login_page_post_response.text)["userId"]
    user_token = json.loads(login_page_post_response.text)["token"]
    # add book
    isbn_number_to_add = "9781593275846"
    BookstoreAPI().post_book_for_user(isbn_number_to_add, user_id, user_token)
    bookstore_page_post_response = BookstoreAPI().post_book_for_user(isbn_number_to_add, user_id, user_token)
    assert bookstore_page_post_response.status_code == HTTPStatus.BAD_REQUEST, f'\nStatus code is not as expected\n' \
                                                                               f'Actual: {bookstore_page_post_response.status_code}' \
                                                                               f'\nExpected: {HTTPStatus.BAD_REQUEST}'
    assert "ISBN already present" in str(bookstore_page_post_response.content)
    # post-cond
    BookstoreAPI().delete_book_for_user(user_id, user_token, isbn_number_to_add)
    LogoutAPI().get_logout_page()


@pytest.mark.positive
def test_delete_book_for_user():
    """
     Description: test checks POST method for book store page in order to delete book
     from user's collection

     Pre-conditions:
     1. Send POST request for login page with user login and password
     2. Extract user id and token from server response
     3. Add book into user's collection

     Steps:
     1. Send POST request to delete a single book from user's collection
     2. Check status code and response reason

     Post-conditions:
     1. Delete book for user
     2. Logout from website

     Expected:
     1. After sending POST request to delete a book from user's list
     we receive HTTPStatus.NO_CONTENT and response reason as 'No Content'
     """
    # pre-conditions
    login_page_post_response = LoginAPI().post_login_user()
    user_id = json.loads(login_page_post_response.text)["userId"]
    user_token = json.loads(login_page_post_response.text)["token"]
    isbn_number_to_add = "9781593275846"
    BookstoreAPI().post_book_for_user(isbn_number_to_add, user_id, user_token)
    # test
    bookstore_page_delete_book_response = BookstoreAPI().delete_book_for_user(user_id, user_token, isbn_number_to_add)

    assert bookstore_page_delete_book_response.status_code == HTTPStatus.NO_CONTENT, f'\nStatus code is not as expected\n' \
                                                                                     f'Actual: {bookstore_page_delete_book_response.status_code}' \
                                                                                     f'\nExpected: {HTTPStatus.NO_CONTENT}'
    assert bookstore_page_delete_book_response.reason == 'No Content'
    # post-cond
    LogoutAPI().get_logout_page()


@pytest.mark.positive
def test_put_book_for_user():
    """
     Description: test checks PUT method for book store page in order to replace book
     in user's collection

     Pre-conditions:
     1. Send POST request for login page with user login and password
     2. Extract user id and token from server response
     3. Add book into user's collection

     Steps:
     1. Send POST request to replace a single book in user's collection by changing ISBN number
     2. Check status code and response reason

     Post-conditions:
     1. Delete book for user
     2. Logout from website

     Expected:
     1. After sending PUT request to change a book in user's collection
     we receive HTTPStatus.OK and response reason as 'OK'
     """
    # pre-conditions
    login_page_post_response = LoginAPI().post_login_user()
    user_id = json.loads(login_page_post_response.text)["userId"]
    user_token = json.loads(login_page_post_response.text)["token"]
    # add book
    isbn_number_to_replace = "9781593275846"
    BookstoreAPI().post_book_for_user(isbn_number_to_replace, user_id, user_token)
    # test
    isbn_number_to_put = "9781491904244"
    bookstore_page_put_response = BookstoreAPI().put_book_for_user(isbn_number_to_replace, isbn_number_to_put,
                                                                   user_id, user_token)
    assert bookstore_page_put_response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\n' \
                                                                     f'Actual: {bookstore_page_put_response.status_code}' \
                                                                     f'\nExpected: {HTTPStatus.OK}'
    assert bookstore_page_put_response.reason == 'OK'
    # post-cond
    BookstoreAPI().delete_book_for_user(user_id, user_token, isbn_number_to_put)
    LogoutAPI().get_logout_page()


@pytest.mark.negative
def test_delete_user_without_token():
    """
     Description: test checks that DELETE method for login page will throw error code
     in case we try to delete user with wrong access token

     Pre-conditions:
     1. Send POST request for login page with user login and password
     2. Extract user id and token from server response

     Steps:
     1. Send DELETE request with token set to None
     2. Check status code and response reason

     Post-conditions:
     1. Logout from website

     Expected:
     1. After sending DELETE request for login page server will throw HTTPStatus.UNAUTHORIZED and reason Unauthorized
     in case we try to delete user with wrong access token
     """
    # pre-conditions
    login_page_post_response = LoginAPI().post_login_user()
    user_id = json.loads(login_page_post_response.text)["userId"]
    user_token = None
    # test
    user_page_delete_response = UserAPI().delete_user(user_id, user_token)
    assert user_page_delete_response.status_code == HTTPStatus.UNAUTHORIZED, f'\nStatus code is not as expected\n' \
                                                                             f'Actual: {user_page_delete_response.status_code}' \
                                                                             f'\nExpected: {HTTPStatus.UNAUTHORIZED}'
    assert user_page_delete_response.reason == 'Unauthorized'

    # post-cond
    LogoutAPI().get_logout_page()


@pytest.mark.positive
def test_delete_user():
    """
     Description: test checks that DELETE method for login page

     Pre-conditions:
     1. Send POST request for login page with user login and password
     2. Extract user id and token from server response

     Steps:
     1. Send DELETE request with correct token
     2. Check status code and response reason

     Expected:
     1. After sending DELETE request for login page will return HTTPStatus.NO_CONTENT and reason No Content
     in case we delete user with correct access token
     """
    # pre-conditions
    login_page_post_response = LoginAPI().post_login_user()
    user_id = json.loads(login_page_post_response.text)["userId"]
    user_token = json.loads(login_page_post_response.text)["token"]
    # test
    user_page_delete_response = UserAPI().delete_user(user_id, user_token)
    assert user_page_delete_response.status_code == HTTPStatus.NO_CONTENT, f'\nStatus code is not as expected\n' \
                                                                           f'Actual: {user_page_delete_response.status_code}' \
                                                                           f'\nExpected: {HTTPStatus.NO_CONTENT}'
    assert user_page_delete_response.reason == 'No Content'
