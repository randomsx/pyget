import chardet


def main():
    j = chardet.detect(b'Hello, X_X')
    print(j)


if __name__ == '__main__':
    main()
