#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0: return False
        m,n = len(nums), sum(nums) // 2
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(
                        dp[i-1][j], # 不选
                        dp[i-1][j-nums[i-1]] + nums[i-1]
                    )
        return dp[m][n] == sum(nums) // 2 # 看能不能装满
# @lc code=end

