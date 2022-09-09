#！ -*-coding: utf-8 -*-
"""
@Author: Gump
@Create Time: 20220909
@Info: 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列
"""

def searchMatrix(matrix, target):
    if not matrix:
        return False

    def bin_search(row_low, row_high, col_low, col_high):
        mid_row = (row_low + row_high) // 2
        mid_col = (col_low + col_high) // 2

        if row_low < row_high and col_low < col_high:
            if matrix[mid_row][mid_col] > target:
                return True if bin_search(row_low, mid_row-1, col_low, col_high) else bin_search(row_low, row_high, col_low, mid_col-1)
            else:
                return True if bin_search(mid_row+1, row_high, col_low, col_high) else bin_search(row_low, row_high, mid_col+1, col_high)

        if matrix[mid_row][mid_col] == target:
            return True

        return False

    return bin_search(0, len(matrix)-1, 0, len(matrix[0])-1)


if __name__ == '__main__':
    test_input = [[3,3,8,13,13,18],
                  [4,5,11,13,18,20],
                  [9,9,14,15,23,23],
                  [13,18,22,22,25,27],
                  [18,22,23,28,30,33],
                  [21,25,28,30,35,35],
                  [24,25,33,36,37,40]]
    test_input1 = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    print(searchMatrix(test_input1, 5))