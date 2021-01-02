from connector.connection import Connection
from connector.http_parser import HTTPParser
from connector.request import HTTPRequest
from connector.url_parser import URLParser


class UrlHandler:
    def get_page_by_url(self, url: str) -> str:
        parser = self._parse_url(url)
        connector = Connection(parser.host, parser.protocol)
        try:
            connector.create_connection()
            request = HTTPRequest.create_request('GET', parser)
            connector.send_message(request)
            answer = connector.get_answer()
        finally:
            connector.close()

        return self._parse_answer(answer, parser)

    @staticmethod
    def _parse_url(url: str) -> URLParser:
        parser = URLParser()
        parser.parse_url(url)
        return parser

    def _parse_answer(self, answer: bytes, parser: URLParser) -> str:
        http_parser = HTTPParser(answer)
        if http_parser.code.startswith('2'):
            return http_parser.body
        elif http_parser.code.startswith('3'):
            location = http_parser.get_location(parser)
            return self.get_page_by_url(location)
        elif http_parser.code.startswith('4') or \
                http_parser.code.startswith('5'):
            return f'Ошибка {http_parser.code}'
