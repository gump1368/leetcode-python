#！ -*- coding: utf-8 -*-
"""
@Author: GUMP
@Create Time: 20230105
@Info:
"""
def divide(dividend: int, divisor: int):
    min_value = -2 ** 31
    max_value = 2 ** 31 - 1

    if divisor == 1:
        return dividend if min_value <= dividend <= max_value else max_value

    if divisor == -1:
        return -dividend if min_value <= -dividend <= max_value else max_value

    sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
    a, b = abs(dividend), abs(divisor)
    res = 0
    while a >= b:
        count = 1
        c = b
        while a > c << 1:
            c <<= 1
            count <<= 1
        res += count
        a -= c
    res = res if sign else -res
    return res-1 if res > max_value else res


if __name__ == '__main__':
    print(divide(10, 3))


