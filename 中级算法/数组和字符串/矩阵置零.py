# ！-*- coding: utf-8 -*-


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        i, j = 0, 0
        i2zero = []
        j2zero = []
        while i < m:
            if matrix[i][j] == 0:
                i2zero.append(i)
                j2zero.append(j)
                for k in range(n):
                    if matrix[i][k] == 0 and k != j:
                        j2zero.append(k)
                i += 1
                j = 0
            else:
                j += 1

            if j == n:
                i += 1
                j = 0

        for i in i2zero:
            for j in range(n):
                matrix[i][j] = 0

        for j in j2zero:
            for i in range(m):
                matrix[i][j] = 0


if __name__ == '__main__':
    solution = Solution()
    mat = [[9,-6,-1,-2,5],[-1,3,2147483647,-4,0],[-3,-4,0,4,-2147483648]]
    solution.setZeroes(mat)
    print(mat)
