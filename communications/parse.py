import argparse


class Parser(argparse.ArgumentParser):
    _help_line = '''HTTP(s)-клиент для получения доступа к
     содержанию страницы по ее URL адресу'''

    def __init__(self):
        super().__init__(description=self._help_line)
        self.add_argument('-f', '--file', type=str, action='store',
                          dest='file', nargs='?',
                          help='Имя файла для записи вывода')

        self.add_argument('url', type=str, action='store',
                          nargs=1,
                          help='URL адрес страницы')
