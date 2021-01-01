import socket
import sys


class ConnectionException(Exception):
    def __init__(self, message: str):
        self._message = message

    def get_msg(self):
        return self._message


class Connection:
    def __init__(self, url: str, port: int):
        self.url = url
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def create_connection(self):
        self.sock.settimeout(5)
        try:
            self.sock.connect((self.url, self.port))
        except socket.timeout:
            raise ConnectionException("Истекло время подключения к серверу")
        except OSError:
            raise ConnectionException("Не удалось установить соединение")

    def send_message(self, msg: str):
        try:
            self.sock.send(msg.encode() + b'\n')
        except OSError:
            raise ConnectionException("Ошибка отправки сообщения")

    def get_answer(self) -> bytes:
        lines = []
        while True:
            try:
                buffer = self.sock.recv(2048)
                lines.append(buffer)
            except socket.timeout:
                break

        return b''.join(lines)

    def close(self):
        self.sock.close()
