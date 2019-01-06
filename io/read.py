import os
import json

def testj():
    obj = dict(name='小明', age=20)
    s = json.dumps(obj, ensure_ascii=False)
    print(s)
    print("你好")


if __name__ == '__main__':
    fpath = '../README.md'
    with open(fpath, 'r') as f:
        print(f.read())
    print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
    testj()