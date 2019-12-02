# connecting to web

import urllib.request
url = "http://www.google.co.uk"


def main():
    web = urllib.request.urlopen(url)
    print("result code: ", web.getcode())

    data = web.read()

    print(data)


if (__name__ == "__main__"):
    main()
