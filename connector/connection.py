import socket

from tools.exceptions import ConnectionException


class Connection:
    def __init__(self, host: str, protocol: str):
        self.host = host
        self.port = 443 if protocol == 'https' else 80
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def create_connection(self):
        self.sock.settimeout(1)
        try:
            self.sock.connect((self.host, self.port))
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
                if not buffer:
                    break
                lines.append(buffer)
            except socket.timeout:
                break

        return b''.join(lines)

    def close(self):
        self.sock.close()
