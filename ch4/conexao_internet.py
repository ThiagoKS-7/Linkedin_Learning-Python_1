import urllib.request


def get_url_response(link=str) -> None:
    obj = urllib.request.urlopen(link)
    if obj.getcode() == 200:
        print(obj.read())


def main():
    get_url_response("http://www.google.com")


if __name__ == '__main__':
    main()
