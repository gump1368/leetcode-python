#！ -*- coding: utf-8 -*-
"""
@Author: GUMP
@Create Time: 20230105
@Info
"""

def fractionToDecimal(numerator: int, denominator: int):
    if numerator % denominator == 0:
        return str(numerator // denominator)

    res = []
    if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
        res.append('-')

    # 整数部分
    numerator = abs(numerator)
    denominator = abs(denominator)
    res.append(str(numerator // denominator))
    res.append('.')

    # 小数部分
    index_map = {}
    remainder = numerator % denominator
    while remainder and remainder not in index_map:
        index_map[remainder] = len(res)
        remainder *= 10
        res.append(str(remainder // denominator))
        remainder = remainder % denominator

    if remainder:
        index = index_map[remainder]
        res.insert(index, '(')
        res.append(')')

    return ''.join(res)

if __name__ == '__main__':
    print(fractionToDecimal(1, 6))
