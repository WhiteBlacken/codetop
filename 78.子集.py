#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 划重点：元素互不相同
        res = []
        def backtrack(start, tmp):
            res.append(tmp.copy())
            for i in range(start, len(nums)):
                tmp.append(nums[i])
                backtrack(i+1, tmp)
                tmp.pop()
        backtrack(0, [])
        return res
# @lc code=end

