#！ -*- coding: utf-8 -*-
"""
@Author: gump
@Create Time: 20220714
@Info: 单词搜索
"""
from typing import List


# def exist(board: List[List[str]], word: str) -> bool:
#     """
#     输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
#     输出：false
#
#     :param board:
#     :param word:
#     :return:
#     """
#     row_length = len(board)
#     col_length = len(board[0])
#     size = row_length * col_length
#
#     def trace_back(value, k, last_position):
#         if k >= len(word) or value < 0:
#             return k
#
#         while value < size:
#             row = value // col_length
#             col = value % col_length
#             if board[row][col] == word[k]:
#                 left = value - 1
#                 right = value + 1
#                 up = value - row_length
#                 down = value + row_length
#                 k += 1
#                 k = trace_back(left, k, 'left') if last_position != 'right' else k
#                 k = trace_back(right, k, 'right') if last_position != 'left' else k
#                 k = trace_back(up, k, 'up') if last_position != 'down' else k
#                 k = trace_back(down, k, 'down') if last_position != 'up' else k
#             else:
#                 value += 1
#
#             if k >= len(word):
#                 break
#
#         return k
#
#     pos = trace_back(0, 0, 'None')
#     return True if pos == len(word) else False


def exist(board: List[List[str]], word: str) -> bool:
    """
    输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    输出：false

    :param board:
    :param word:
    :return:
    """
    row_length = len(board)
    col_length = len(board[0])

    def trace_back(i, j, k, temp_path):
        if (i, j) in temp_path:
            return k - 1
        if k >= len(word):
            return k

        temp_path.append((i, j))
        depth = k
        if j-1 >= 0 and board[i][j-1] == word[k]:
            temp_1 = trace_back(i, j-1, k+1, temp_path)
            depth = temp_1 if temp_1 > depth else depth
        if j+1 < col_length and board[i][j+1] == word[k]:
            temp_1 = trace_back(i, j+1, k + 1, temp_path)
            depth = temp_1 if temp_1 > depth else depth
        if i-1 >= 0 and board[i-1][j] == word[k]:
            temp_1 = trace_back(i-1, j, k+1,  temp_path)
            depth = temp_1 if temp_1 > depth else depth
        if i+1 < row_length and board[i+1][j] == word[k]:
            temp_1 = trace_back(i+1, j, k+1, temp_path)
            depth = temp_1 if temp_1 > depth else depth


        temp_path.pop(-1)

        return depth

    for row in range(row_length):
        for col in range(col_length):
            if board[row][col] == word[0]:
                pos = trace_back(row, col, 1,  [])
                if pos >= len(word):
                    return True

    return False


if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(exist(board, word))