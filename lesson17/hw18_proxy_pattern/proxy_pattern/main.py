from lesson17.hw18_proxy_pattern.proxy_pattern.proxy_txt_writer import TxtProxyReaderWriter
from lesson17.hw18_proxy_pattern.proxy_pattern.txt_reader import TxtReader
from lesson17.hw18_proxy_pattern.proxy_pattern.txt_writer import TxtWriter


txt_reader = TxtReader('users.txt')
txt_writer = TxtWriter('users.txt')
proxy_reader_writer = TxtProxyReaderWriter(txt_writer, txt_reader)

proxy_reader_writer.write_file('\nhello teacher!')
print(proxy_reader_writer.read_file())
print('\n')
proxy_reader_writer.write_file('\nhello teacher_2!')
print(proxy_reader_writer.read_file())
print('\n')
print(proxy_reader_writer.read_file())
