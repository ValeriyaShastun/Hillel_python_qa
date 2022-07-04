from lesson17.hw18_proxy_pattern.proxy_pattern.abstract_writer import Writer
from lesson17.hw18_proxy_pattern.proxy_pattern.txt_writer import TxtWriter
from lesson17.hw18_proxy_pattern.proxy_pattern.abstract_reader import Reader
from lesson17.hw18_proxy_pattern.proxy_pattern.txt_reader import TxtReader


class TxtProxyReaderWriter(Writer, Reader):
    def __init__(self, txt_writer: TxtWriter, txt_reader: TxtReader):
        self.__result = ''
        self.__is_actual = False
        self.__writer = txt_writer
        self.__reader = txt_reader

    def write_file(self, new_data):
        self.__result = self.__writer.write_file(new_data)
        self.__is_actual = False

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__reader.read_file()
            self.__is_actual = True
            return self.__result

    def update_actual_status(self, status):
        self.__is_actual = status

