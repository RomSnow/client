from connector.connection import Connection, ConnectionException
from communications.console_reader import ConsoleReader
import sys


def main(url: str, port: int = 80):
    connect = Connection(url, port)
    reader = ConsoleReader()
    try:
        connect.create_connection()
        while True:
            message = reader.get_user_message()
            if not reader.is_ready:
                break
            connect.send_message(message)
            print(connect.get_answer() + b'\n\n')
    except ConnectionException as e:
        print(e.get_msg())
    finally:
        connect.close()


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))
