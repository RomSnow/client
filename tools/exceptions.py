class MyException(Exception):
    def __init__(self, message: str):
        self._message = message

    def get_msg(self) -> str:
        return self._message


class ConnectionException(MyException):
    def __init__(self, message: str):
        super().__init__(message)


class ParseException(MyException):
    def __init__(self, message: str):
        super().__init__(message)
