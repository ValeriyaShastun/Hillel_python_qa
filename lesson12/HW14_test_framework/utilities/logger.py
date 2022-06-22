from lesson12.HW14_test_framework.utilities.read_run_settings import ReadConfig
import logging


class Logger():
    @staticmethod
    def getLogger():
        return Logger.logger


Logger.logger = logging.getLogger()
Logger.logger.setLevel(ReadConfig.get_logger())
