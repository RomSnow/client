import unittest
from connector.http_parser import HTTPParser


class ConnectorTestCases(unittest.TestCase):
    def setUp(self):
        with open('test_ans.txt') as file:
            self.text = file.read().encode()

    def test_http_parser(self):
        parser = HTTPParser(self.text)

        self.assertEqual(parser.code, '200')
        self.assertEqual(parser.protocol, 'HTTP')
        self.assertEqual(parser.version, '1.1')

        self.assertTrue(parser.body.startswith('5257'))


if __name__ == '__main__':
    unittest.main()
