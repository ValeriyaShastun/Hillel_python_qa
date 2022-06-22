from lesson12.HW14_test_framework.CONSTS import ROOT_DIR
import configparser
import os

abs_path = os.path.abspath(fr"{ROOT_DIR}/configurations/configuration.ini")
config = configparser.RawConfigParser()
config.read(abs_path)


class ReadConfig:
    @staticmethod
    def get_application_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_driver_id():
        return config.get('browser', 'browser_id')

    @staticmethod
    def get_headless_mod():
        return config.get('browser', 'is_headless')

    @staticmethod
    def get_logger():
        return config.get('logger', 'level')
