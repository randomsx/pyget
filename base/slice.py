def findMinAndMax(L):
    if len(L) < 1:
        return None, None
    ma = max(L)
    mi = min(L)
    return mi, ma


def judge():
    L = ['Hello', 'World', 18, 'Apple', None]
    return [s.lower() for s in L if isinstance(s, str)]


if __name__ == '__main__':
    # 测试
    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')

    print("############")
    L2 = judge()
    if L2 == ['hello', 'world', 'apple']:
        print('测试通过!')
    else:
        print('测试失败!')
