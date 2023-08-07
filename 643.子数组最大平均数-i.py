#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float('-inf')
        prefix = [0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            prefix[i] = prefix[i-1] + nums[i-1]
            if i >= k:
                res = max(res, (prefix[i]-prefix[i-k])/k)
        return res


# @lc code=end

