from lesson17.hw18_proxy_pattern.proxy_pattern.abstract_writer import Writer
from lesson17.hw18_proxy_pattern.proxy_pattern.txt_writer import TxtWriter


class TxtProxyWriter(Writer):
    def __init__(self, txt_writer: TxtWriter):
        self.__result = ''
        self.__is_actual = False
        self.__writer = txt_writer

    def write_file(self, new_data):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__writer.write_file(new_data)
            self.__is_actual = True
            return self.__result

    def update_actual_status(self, status):
        self.__is_actual = status
