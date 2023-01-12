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

    def bin_search(arrs, low, high):
        if not row[0] <= target <= row[-1] or not arrs:
            return False, None
        mid = (low + high) // 2
        if low < high:
            if arrs[mid] < target:
                return bin_search(arrs, mid+1, high)
            else:
                return bin_search(arrs, low, mid)
        if arrs[mid] == target:
            return True, mid
        return False, mid

    for i, row in enumerate(matrix):
        flag, index = bin_search(row, 0, len(row)-1)
        if flag:
            return True
        if not index:
            continue
        col_rows = [_row[index] for _row in matrix[i+1:]]
        flag, index = bin_search(col_rows, 0, len(col_rows)-1)
        if flag:
            return True

    return False





    # def bin_search(row_low, row_high, col_low, col_high):
    #     mid_row = (row_low + row_high) // 2
    #     mid_col = (col_low + col_high) // 2
    #
    #     if row_low < row_high and col_low < col_high:
    #         if matrix[mid_row][mid_col] > target:
    #             return True if bin_search(row_low, mid_row-1, col_low, col_high) else bin_search(row_low, row_high, col_low, mid_col-1)
    #         else:
    #             return True if bin_search(mid_row+1, row_high, col_low, col_high) else bin_search(row_low, row_high, mid_col+1, col_high)
    #
    #     if matrix[mid_row][mid_col] == target:
    #         return True
    #
    #     return False

    # return bin_search(0, len(matrix)-1, 0, len(matrix[0])-1)


if __name__ == '__main__':
    test_input = [[1,4,7,11,15],
                  [2,5,8,12,19],
                  [3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    print(searchMatrix(test_input, 20))