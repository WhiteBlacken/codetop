#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 子数组：连续，又要求和，考虑前缀和
        dict = {} # 记录次数
        sum_val = res = 0
        dict[sum_val] = 1
        for item in nums:
            sum_val += item
            if (sum_val - k) in dict: # 前缀和，表示中间一段为k
                res += dict[sum_val - k] # 有几种，就有几种子数组，起点不同，终点相同
            dict[sum_val] = dict.get(sum_val, 0) + 1 # 出现该值的字数
        return res
        

# @lc code=end

