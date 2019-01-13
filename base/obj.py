# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    __slots__ = ('width', 'height')

    @property
    def resolution(self):
        return 786432


if __name__ == '__main__':
    # 测试:
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')
