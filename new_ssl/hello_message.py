import socket
import time
import random


class TLSHelloMessage:
    def __init__(self):
        self.key = ''

    def generate_message(self):
        con_type = b'\x16'
        version = b'\x03\x03'
        pack_len = b'\x00\x2f'
        byte = b'\x01'
        length = b'\x00\x00\x2b'
        timestamp = int(time.time()).to_bytes(4, 'big')
        random_key = self._get_random_bytes(28)
        session_di = b'\x00'
        suitcase_len = b'\x00\x02'
        cipher_suit_case = b'\xc0\x2f'
        compression_methods_len = b'\x01'
        compression_methods = b'\x00'
        extensions_len = b'\x00\x00'

        return b''.join((con_type, version, pack_len, byte, length, version,
                         timestamp, random_key, session_di, suitcase_len,
                         cipher_suit_case, compression_methods_len,
                         compression_methods, extensions_len))

    @staticmethod
    def _get_random_bytes(length: int):
        random_lines = []
        for i in range(length):
            rand = random.randrange(0, 16)
            brand = rand.to_bytes(1, 'big')
            random_lines.append(brand)

        return b''.join(random_lines)


if __name__ == '__main__':
    msg = TLSHelloMessage().generate_message()

    sock = socket.create_connection(('www.python.org', 443))
    sock.settimeout(1)
    sock.sendall(msg)
    while True:
        try:
            buff = sock.recv(4096)
            if not buff:
                break
            print(buff, end='')
        except socket.timeout:
            break

