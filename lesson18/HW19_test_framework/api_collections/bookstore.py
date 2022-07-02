import json
from lesson18.HW19_test_framework.utilities.web_api.base_api import BaseAPI
from lesson18.HW19_test_framework.utilities.decorators import HelperDecorators as decorator


@decorator.auto_steps
class BookstoreAPI(BaseAPI):

    def __init__(self):
        super().__init__()
        self.books_url = "BookStore/v1/Books"
        self.book_url = "BookStore/v1/Book"

    def post_book_for_user(self, isbn_number, user_id, user_token):
        return self.post(url=f"{self.books_url}",
                         body=json.dumps({"userId":f"{user_id}","collectionOfIsbns":[{"isbn":f"{isbn_number}"}]}),
                         headers={"Content-Type": "application/json", "Authorization":"Bearer "+f"{user_token}"})

    def post_books_for_user(self, user_id, user_token, **kwargs):
        isbn_collection = [{"isbn":f"{kwargs.get(isbn_number)}"} for isbn_number in kwargs]
        return self.post(url=f"{self.books_url}",
                         body=json.dumps({"userId":f"{user_id}","collectionOfIsbns":isbn_collection}),
                         headers={"Content-Type": "application/json", "Authorization":"Bearer "+f"{user_token}"})

    def put_book_for_user(self, isbn_number_to_replace, isbn_number_to_put, user_id, user_token):
        book_url = f"/{isbn_number_to_replace}"
        return self.put(url=f"{self.books_url}{book_url}",
                        body=json.dumps({"userId": f"{user_id}","isbn": f"{isbn_number_to_put}"}),
                        headers={"Content-Type": "application/json", "accept": "application/json",
                                 "Authorization":"Bearer "+f"{user_token}"})

    def delete_book_for_user(self, user_id, user_token, isbn_number):
        return self.delete(url=f"{self.book_url}",
                           body=json.dumps({"isbn":f"{isbn_number}","userId":f"{user_id}"}),
                           headers={"Content-Type": "application/json",
                                    "Authorization":"Bearer "+f"{user_token}"})
