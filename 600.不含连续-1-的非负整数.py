#
# @lc app=leetcode.cn id=600 lang=python3
#
# [600] 不含连续1的非负整数
#

# @lc code=start
class Solution:
    def findIntegers(self, n: int) -> int:
        self.nums = list(map(int, bin(n)[2:]))
        return self.dp(0, 0, True)

    @lru_cache(None)
    def dp(self, index, pre_bit, limit):
        if index == len(self.nums):
            return 1
        up = self.nums[index] if limit else 1
        ans = 0
        for i in range(up+1):
            if i == 1 and pre_bit == 1:
                continue
            ans += self.dp(index+1, i, limit and i == up)
        return ans
    

# @lc code=end

