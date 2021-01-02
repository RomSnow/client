import unittest

from communications.handler import UrlHandler


class TestCommunicationCase(unittest.TestCase):
    def test_get_page_by_url(self):
        body = UrlHandler().get_page_by_url('http://kmath.ru/')
        with open('test_ans.txt') as file:
            text = file.read()
        self.assertTrue(body.startswith('<HTML>'))


if __name__ == '__main__':
    unittest.main()
