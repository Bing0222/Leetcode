"""
给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。

输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,4,7,5,3,6,8,9]
"""


class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        for i in range(m + n - 1):
            if i % 2 == 0:
                for j in range(min(i, m - 1), max(-1, i - n), -1):
                    res.append(matrix[j][i - j])
            else:
                for j in range(min(i, n - 1), max(-1, i - m), -1):
                    res.append(matrix[i - j][j])

        return res


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(Solution().findDiagonalOrder(mat))
