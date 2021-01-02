from connector.url_parser import URLParser


class HTTPRequest:
    @staticmethod
    def create_request(request_type: str, parser: URLParser):
        main_line = f'{request_type} {parser.resource} HTTP/1.1'
        host_line = f'Host: {parser.host}'
        connection_line = 'Connection: close'

        return '\r\n'.join((main_line, host_line, connection_line, '\r\n'))
