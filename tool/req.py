import requests


def main():
    same()


def same():
    r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like '
                                                                       'Mac OS X) AppleWebKit'}, timeout=9)
    print(r.status_code)
    print(r.encoding)


if __name__ == '__main__':
    main()
