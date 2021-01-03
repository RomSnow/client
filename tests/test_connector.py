import socket
import unittest
from connector.http_parser import HTTPParser
from connector.request import HTTPRequest
from connector.url_parser import URLParser
from connector.connection import Connection
from tools.exceptions import MyException


class ConnectorTestCases(unittest.TestCase):
    def setUp(self):
        self.text = \
            b'HTTP/1.1 302 Found\r\n' \
            b'Date: Sat, 02 Jan 2021 17:04:18 GMT\r\n' \
            b'Server: Apache/2.4.6 (CentOS)' \
            b' OpenSSL/1.0.2k-fips PHP/5.4.16\r\n' \
            b'X-Powered-By: PHP/5.4.16\r\nLocation: news.php\r\n' \
            b'Content-Length: 0\r\n' \
            b'Content-Type: text/html; charset=Windows-1251\r\n\r\n'

    def test_http_parser(self):
        parser = HTTPParser(self.text)

        self.assertEqual(parser.code, '302')
        self.assertEqual(parser.protocol, 'HTTP')
        self.assertEqual(parser.version, '1.1')

        self.assertTrue(not parser.body)

    def test_url_parser(self):
        parser = URLParser()
        parser.parse_url('http://www.google.com/')
        self.assertEqual(parser.protocol, 'http')
        self.assertEqual(parser.host, 'www.google.com')
        self.assertEqual(parser.resource, '/')

        self.assertRaises(MyException, parser.parse_url, ('http:/hi.m',))

    def test_request(self):
        parser = URLParser()
        parser.parse_url('http://www.google.com/')

        request = 'GET / HTTP/1.1\r\n' \
                  'Host: www.google.com\r\n' \
                  'Connection: close\r\n\r\n'

        self.assertEqual(HTTPRequest.create_request('GET', parser), request)

    def test_connection(self):
        connection = Connection('kmath.ru', 'http')
        connection.create_connection()
        connection.send_message('GET / HTTP/1.1\r\nHost: kmath.ru\r\n\r\n')
        ans = connection.get_answer()
        self.assertTrue(ans.startswith(b'HTTP/1.1 200'))

    def test_https(self):
        connection = Connection('www.google.com', 'https')
        connection.create_connection()
        connection.send_message('GET / HTTP/1.1\r\n'
                                'Host: www.google.com\r\n\r\n')
        ans = connection.get_answer()
        self.assertTrue(ans.startswith(b'HTTP/1.1 200'))


if __name__ == '__main__':
    unittest.main()
