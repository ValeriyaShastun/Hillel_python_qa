from lesson18.HW19_test_framework.utilities.read_run_settings import ReadConfig
from lesson18.HW19_test_framework.utilities.logger import Logger as logger
import requests


class BaseAPI:

    def __init__(self):
        self.base_url = ReadConfig.get_application_url()
        self.name = ReadConfig.get_user_name()
        self.password = ReadConfig.get_user_password()
        self.headers = {'Accept': '*/*'}
        self.request = requests
        self.logger = logger.getLogger()

    def get(self, url, body=None, headers=None, params=None):
        if headers is None:
            headers = self.headers
        response = self.request.get(f"{self.base_url}{url}", data=body, headers=headers, params=params)
        self.logger.info(f'Perform GET request')
        return response

    def post(self, url, body=None, headers=None, params=None):
        if headers is None:
            headers = self.headers
        response = self.request.post(f"{self.base_url}{url}", data=body, headers=headers, params=params)
        self.logger.info(f'Perform POST request')
        return response

    def delete(self, url, body=None, headers=None, params=None):
        if headers is None:
            headers = self.headers
        response = self.request.delete(f"{self.base_url}{url}", data=body, headers=headers, params=params)
        self.logger.info(f'Perform DELETE request')
        return response

    def put(self, url, body=None, headers=None, params=None):
        if headers is None:
            headers = self.headers
        response = self.request.put(f"{self.base_url}{url}", data=body, headers=headers, params=params)
        self.logger.info(f'Perform PUT request')
        return response
