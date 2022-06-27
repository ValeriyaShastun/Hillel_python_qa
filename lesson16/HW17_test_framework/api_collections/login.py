import json

from lesson16.HW17_test_framework.utilities.web_api.base_api import BaseAPI


class LoginAPI(BaseAPI):

    def __init__(self):
        super().__init__()
        self.login_url = "Account/v1/Login"

    def get_login_page(self):
        return self.get(url=f"{self.login_url}")

    def post_login_user(self):
        return self.post(url=f"{self.login_url}", body=json.dumps({"userName": f"{self.name}",
                                                                   "password": f"{self.password}"}),
                         headers={"Content-Type": "application/json"})
