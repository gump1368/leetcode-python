#！ -*- coding: utf-8 -*-
"""
@Author: Gump
@Create Time: 20220915
@Info:
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
"""

def uniquePaths(m, n):
    """
    输入：m = 3, n = 7
    输出：28
    :param m:
    :param n:
    :return:
    """
    dp = [[1]]
    for i in range(m):
        if i > 0:
            dp.append([])
        for j in range(n):
            if i == 0 and j == 0:
                continue
            value1 = dp[i-1][j] if i > 0 else 0
            value2 = dp[i][j-1] if j > 0 else 0
            dp[i].append(value1 + value2)

    return dp[-1][-1]


if __name__ == '__main__':
    print(uniquePaths(3, 3))
