#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        res = []

        while top <= bottom and left <= right:
            for j in range(left, right+1):
                res.append(matrix[top][j])
            for i in range(top+1, bottom+1):
                res.append(matrix[i][right])
            if top < bottom:
                for j in range(right-1,left-1,-1):
                    res.append(matrix[bottom][j])
            if left < right:
                for i in range(bottom -1,top,-1):
                    res.append(matrix[i][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return res
# @lc code=end

