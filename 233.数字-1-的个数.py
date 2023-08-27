#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        self.memx = {}
        res = [int(x) for x in str(n)]
        return self.dp(0, True, res)
    
    def dp(self, index, limit, num_list):
        if (index,limit) in self.memx:
            return self.memx[(index, limit)]
        if index == len(num_list): # base case
            return 0
        
        up = num_list[index] if limit else 9
        ans = 0
        for i in range(up+1):
            if i == 1:
                if index == len(num_list) - 1:
                    ans += 1
                else:
                    if limit and i == up:
                        ans += int("".join(map(str, num_list[index+1:]))) + 1
                    else:
                        ans += 10**(len(num_list) - index - 1)
            ans += self.dp(index+1, limit and i==up, num_list)
        self.memx[(index,limit)] = ans
        return ans
    
# @lc code=end

