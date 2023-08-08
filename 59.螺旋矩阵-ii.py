#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 螺旋矩阵1的逆向操作
        res = [[0]*n for _ in range(n)]
        top, bottom, left, right = 0, n-1, 0, n-1

        num = 1
        while top <= bottom and left <= right:
            for j in range(left, right+1):
                res[top][j] = num
                num += 1
            for i in range(top+1, bottom+1):
                res[i][right] = num
                num += 1
            if top < bottom:
                for j in range(right-1, left-1, -1):
                    res[bottom][j] = num
                    num += 1
            if left < right:
                for i in range(bottom-1, top, -1):
                    res[i][left] = num
                    num += 1
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return res
# @lc code=end

