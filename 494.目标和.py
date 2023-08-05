#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        爆搜能做，超时
        难的是将他理解成01背包问题
        状态：剩余容量，但是会变大？
        选择：当前选+，还是选-
        """
# @lc code=end

