#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 涨就买
        sum_val = 0
        for i in range(len(prices)):
            if i == 0: continue
            if prices[i] - prices[i-1] > 0:
                sum_val += prices[i] - prices[i-1]
        return sum_val

# @lc code=end

