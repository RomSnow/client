from communications.handler import UrlHandler
from tools.exceptions import MyException


def main(url: str):
    try:
        answer = UrlHandler().get_page_by_url(url)
        print(answer)
    except MyException as exc:
        print(exc.get_msg())


if __name__ == '__main__':
    main('http://kadm.kmath.ru/')
    # main('http://www.google.com/')
