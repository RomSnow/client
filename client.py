import sys

from communications.handler import UrlHandler
from tools.exceptions import MyException
from communications.parse import Parser


def main(args: list):
    parser = Parser()
    arg = parser.parse_args(args)
    try:
        answer = UrlHandler().get_page_by_url(arg.url[0])
        write_file = sys.stdout
        if arg.file:
            write_file = open(arg.file, 'w')

        print(answer, file=write_file)
        write_file.close()
    except MyException as exc:
        print(exc.get_msg())


if __name__ == '__main__':
    main(sys.argv[1:])
