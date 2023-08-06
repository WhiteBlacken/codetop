#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 只有卖出，带冷冻的股票问题
        # dp[i][j]: 在第i家执行j操作，剩余的钱数,可以缩减
        # dp[i]: 在第i家的钱财最大值
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            if i == 0:  # base case
                dp[i] = nums[i]
                continue
            if i == 1:  # base case
                dp[i] = max(nums[i], nums[i - 1])  # 要么第一天偷，要么第二天偷
                continue
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])  # 不偷，在i-1操作  # 偷了的话，只能大前天操作了
        print(dp)
        return dp[n - 1]


# @lc code=end
