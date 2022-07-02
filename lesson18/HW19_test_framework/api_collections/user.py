from lesson18.HW19_test_framework.utilities.web_api.base_api import BaseAPI
from lesson18.HW19_test_framework.utilities.decorators import HelperDecorators as decorator


@decorator.auto_steps
class UserAPI(BaseAPI):

    def __init__(self):
        super().__init__()
        self.delete_url = "Account/v1/User"

    def delete_user(self, user_id, user_token):
        return self.delete(url=f"{self.delete_url}/{user_id}", headers={"Authorization":"Bearer "+f"{user_token}"})
