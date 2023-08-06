#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 与打家截舍I的区别，首尾相连
        # 难点就在于怎么保证首尾互斥->干脆拆开就行
        if len(nums) == 1: return nums[0]
        n = len(nums)
        return max(self.rob_1(nums[:n-1]), self.rob_1(nums[1:]))
    
    def rob_1(self, nums): # 打家劫舍I
        dp = [0]*len(nums)
        for i in range(len(dp)):
            if i == 0: # base case
                dp[i] = nums[i]
                continue
            if i == 1: # base case
                dp[i] = max(nums[i], nums[i-1])
                continue
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[len(dp)-1]
# @lc code=end

