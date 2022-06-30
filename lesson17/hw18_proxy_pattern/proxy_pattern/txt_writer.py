from lesson17.hw18_proxy_pattern.proxy_pattern.abstract_writer import Writer


class TxtWriter(Writer):

    def __init__(self, file_name):
        self.file_name = file_name

    def write_file(self, new_data):
        with open(self.file_name, "a") as file:
            file.write(new_data)
