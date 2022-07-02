from lesson18.HW19_test_framework.utilities.web_api.base_api import BaseAPI
from lesson18.HW19_test_framework.utilities.decorators import HelperDecorators as decorator


@decorator.auto_steps
class LogoutAPI(BaseAPI):

    def __init__(self):
        super().__init__()
        self.logout_url = "favicon.ico"

    def get_logout_page(self):
        return self.get(url=f"{self.logout_url}")
