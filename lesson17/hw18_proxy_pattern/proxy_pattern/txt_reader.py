from lesson17.hw18_proxy_pattern.proxy_pattern.abstract_reader import Reader


class TxtReader(Reader):

    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        with open(self.file_name) as file:
            text = file.read()
        return text
