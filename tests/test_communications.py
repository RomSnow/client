import unittest

from communications.handler import UrlHandler
from communications.parse import Parser


class TestCommunicationCase(unittest.TestCase):
    def test_get_page_by_url(self):
        body = UrlHandler().get_page_by_url('http://kmath.ru/')
        self.assertTrue(body.startswith('<HTML>'))

    def test_parse(self):
        parser = Parser()

        args = parser.parse_args(['-f', 'file', 'http://google.com/'])
        self.assertEqual(args.url[0], 'http://google.com/')
        self.assertEqual(args.file, 'file')


if __name__ == '__main__':
    unittest.main()
