from lesson17.hw18_proxy_pattern.proxy_pattern.proxy_txt_reader import TxtProxyReader
from lesson17.hw18_proxy_pattern.proxy_pattern.proxy_txt_writer import TxtProxyWriter
from lesson17.hw18_proxy_pattern.proxy_pattern.txt_reader import TxtReader
from lesson17.hw18_proxy_pattern.proxy_pattern.txt_writer import TxtWriter


txt_reader = TxtReader('users.txt')
proxy_reader = TxtProxyReader(txt_reader)
txt_writer = TxtWriter('users.txt')
proxy_writer = TxtProxyWriter(txt_writer)

proxy_writer.write_file('\nhello teacher!')
print(proxy_reader.read_file())
print('\n')
proxy_writer.write_file('\nhello teacher!')
print(proxy_reader.read_file())
