#
# @lc app=leetcode.cn id=2560 lang=python3
#
# [2560] 打家劫舍 IV
#

# @lc code=start
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # 冷却期是打家劫舍的基本要求
        # 应该还是个基本的dp
        # dp[i][j]： 在第i个房屋，j次偷窃最小的偷窃能力
        # 0次偷窃的base case怎么办
        n = len(nums)
        if k == 0:
            return 0
        if n == 0:
            return float('inf')
        if n < k:
            return sum(nums)

        # 初始化 dp 数组
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # 不窃取当前房屋
                dp[i][j] = min(dp[i][j], dp[i-1][j])
                # 窃取当前房屋
                if i >= 2:
                    dp[i][j] = min(dp[i][j], dp[i-2][j-1] + nums[i-1])
                else:
                    dp[i][j] = min(dp[i][j], nums[i-1])

        return dp[n][k]

# @lc code=end

