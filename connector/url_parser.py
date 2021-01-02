import re

from tools.exceptions import ParseException


class URLParser:
    def __init__(self):
        self._protocol = ''
        self._host = ''
        self._resource = ''

    def parse_url(self, url: str):

        try:
            match = re.match(
                r'^(?P<protocol>\w*?)://(?P<host>.*?\.\w*?)(?P<resource>/.*)',
                url
            )
            self._protocol = match.group('protocol')
            self._host = match.group('host')
            self._resource = match.group('resource')
        except (AttributeError, TypeError):
            raise ParseException('Неверный формат адресса!')

        if not self._protocol or not self._host or not self._resource:
            raise ParseException('Неверный формат адресса!')

    @property
    def protocol(self):
        return self._protocol

    @property
    def host(self):
        return self._host

    @property
    def resource(self):
        return self._resource
