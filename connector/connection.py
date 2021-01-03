import socket

import ssl
from tools.exceptions import ConnectionException


class Connection:
    def __init__(self, host: str, protocol: str):
        self._protocol = protocol
        self.host = host
        self.port = 443 if protocol == 'https' else 80
        self.connection = None

    def create_connection(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        self.connection = sock
        if self._protocol == 'https':
            self.context = ssl.create_default_context()
            self.connection = ssl.wrap_socket(sock)

        try:
            self.connection.connect((self.host, self.port))
        except socket.timeout:
            raise ConnectionException("Истекло время подключения к серверу")
        except OSError:
            raise ConnectionException("Не удалось установить соединение")

        if self._protocol == 'https':
            self.cert = self.connection.getpeercert()

    def send_message(self, msg: str):
        try:
            self.connection.sendall(msg.encode() + b'\n')
        except OSError:
            raise ConnectionException("Ошибка отправки сообщения")

    def get_answer(self) -> bytes:
        lines = []
        while True:
            try:
                buffer = self.connection.recv(2048)
                if not buffer:
                    break
                lines.append(buffer)
            except socket.timeout:
                break

        return b''.join(lines)

    def close(self):
        self.connection.close()
