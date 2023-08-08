#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#


# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 一个结论：斜对角翻转+中轴线翻转
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        l_col, r_col = 0, n - 1
        while l_col < r_col:
            for i in range(n):
                matrix[i][l_col], matrix[i][r_col] = matrix[i][r_col], matrix[i][l_col]
            l_col += 1
            r_col -= 1


# @lc code=end
