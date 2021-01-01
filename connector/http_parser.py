import re


class HTTPParser:

    def __init__(self, text: bytes):
        self._text = text
        self._protocol: str
        self._version: str
        self._code: str
        self._parse(text)
        self._body = ''

    def _parse(self, text: bytes):
        match = re.match(
            rb'^(?P<protocol>\w*)/(?P<version>\d.\d) (?P<code>\d\d\d)', text)

        self._protocol = match.group('protocol').decode()
        self._version = match.group('version').decode()
        self._code = match.group('code').decode()

    @property
    def body(self):
        if not self._body:
            self._body = self._get_body()
        return self._body

    @property
    def protocol(self):
        return self._protocol

    @property
    def version(self):
        return self._version

    @property
    def code(self):
        return self._code

    def _get_body(self) -> str:
        start_index = self._text.find(rb'\r\n\r\n') + 8
        body = self._text[start_index:]

        charset = re.findall(rb'charset=(.*?)\\r\\n', self._text)[0].decode()
        if not charset:
            charset = 'utf-8'

        return body.decode(charset)
