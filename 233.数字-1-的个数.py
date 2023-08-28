#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        self.s = str(n)
        return self.dp(0, True, 0)
    
    @cache
    def dp(self, index, limit, cnt1):
        if index == len(self.s):
            return cnt1
        res = 0
        up = int(self.s[index]) if limit else 9
        for i in range(up+1):
            res += self.dp(index+1, limit and i==up, cnt1+(i==1))
        return res


    
# @lc code=end

