import json

from lesson16.HW17_test_framework.utilities.web_api.base_api import BaseAPI


class LogoutAPI(BaseAPI):

    def __init__(self):
        super().__init__()
        self.logout_url = "favicon.ico"

    def get_logout_page(self):
        return self.get(url=f"{self.logout_url}")
