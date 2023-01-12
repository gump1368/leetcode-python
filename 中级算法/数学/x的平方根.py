#！ -*- coding: utf-8 -*-
"""
@Author: GUMP
@Create Time: 20230104
@Info:
"""

def mySqrt(x: int) -> int:
    def bin_2(min_value, max_value):
        if min_value > max_value:
            return max_value
        mid = (min_value + max_value) // 2
        value = mid * mid
        if value == x:
            return mid
        elif mid * mid > x:
            return bin_2(min_value, mid - 1)
        else:
            return bin_2(mid + 1, max_value)

    return bin_2(0, x)

if __name__ == '__main__':
    print(mySqrt(100))