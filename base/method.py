def product(x, *args):
    res = x
    for arg in args:
        res *= arg
    return res


def main():
    # 测试
    print('product(5) =', product(5))
    print('product(5, 6) =', product(5, 6))
    print('product(5, 6, 7) =', product(5, 6, 7))
    print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
    if product(5) != 5:
        print('测试失败!')
    elif product(5, 6) != 30:
        print('测试失败!')
    elif product(5, 6, 7) != 210:
        print('测试失败!')
    elif product(5, 6, 7, 9) != 1890:
        print('测试失败!')
    else:
        try:
            product()
            print('测试失败!')
        except TypeError:
            print('测试成功!')


if __name__ == '__main__':
    main()
