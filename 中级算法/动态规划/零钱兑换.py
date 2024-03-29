#！ -*- coding: utf-8 -*-
"""
@author: gump
@create time: 20221208
@info: 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。
"""


def coinChange(coins, amount):
    """
    输入：coins = [1, 2, 5], amount = 11
    输出：3
    解释：11 = 5 + 5 + 1
    :param coins:
    :param amount:
    :return:
    """
    dp = [0]
    for i in range(1, amount+1):
        min_value = float('inf')
        for coin in coins:
            if i - coin >= 0:
                min_value = min(min_value, dp[i-coin]+1)

        dp.append(min_value)

    return -1 if dp[-1] == float('inf') else dp[-1]


if __name__ == '__main__':
    test_input = [1]
    print(coinChange(test_input, 11))



