#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        0-1背包：石头分两堆，尽可能接近，就是其中一堆尽可能接近1/2
        状态：剩余背包容量，其实是剩余可装载的石头重要
        选择：选不选石头
        """
        weight = sum(stones)
        m,n = len(stones), weight // 2
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if j-stones[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(
                        dp[i-1][j],
                        dp[i-1][j-stones[i-1]] + stones[i-1]
                    )
        return weight - 2 * dp[m][n] # 这一步还是不太懂

# @lc code=end

