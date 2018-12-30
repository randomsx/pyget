"""
this file is for data convert
"""

import math
import re
from datetime import datetime, timedelta, timezone


def main():
    print("Doday give me zhu!")
    pass


def to_timestamp(dt_str, tz_str):
    time = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")

    list = re.split(r"[+\-]", tz_str)
    for l in list:
        print(l)

    z = tz_str[0:3]
    flag = tz_str[3]
    delta = int(tz_str[4:].split(":")[0])

    # print(z)
    # print(flag)
    # print(delta)

    if z != "UTC":
        print("Come on, give me CTS!")
        return 0

    if flag == "-":
        delta *= -1

    zon = timezone(timedelta(hours=delta))
    t2 = time.replace(tzinfo=zon)

    return t2.timestamp()


if __name__ == '__main__':
    print("123")
    a = math.pow(10, 100)
    print(a)

    main()
    t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
    assert t1 == 1433121030.0, t1
    t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
    assert t2 == 1433121030.0, t2
    print('ok')
