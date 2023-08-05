#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 划重点：无重复数字，不可使用多次
        # 比I，II更简单了？
        # 子集问题
        res = []
        def backtrack(start, tmp):
            if len(tmp) > k or sum(tmp) > n: return
            if sum(tmp) == n and len(tmp) == k:
                res.append(tmp.copy())
                return
            for i in range(start, 9):
                tmp.append(i+1)
                backtrack(i+1, tmp)
                tmp.pop()
        backtrack(0, [])
        return res
# @lc code=end

