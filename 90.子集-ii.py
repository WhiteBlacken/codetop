#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 划重点：包含重复元素
        res = []
        nums.sort() # diff
        def backtrack(start, tmp):
            res.append(tmp.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i-1] == nums[i]: # diff 保证在同一层不重复
                    continue
                tmp.append(nums[i])
                backtrack(i+1, tmp)
                tmp.pop()
        backtrack(0, [])
        return res
# @lc code=end

