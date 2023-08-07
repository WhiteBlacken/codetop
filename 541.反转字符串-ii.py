#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # 这多少是个指针问题
        # 记录begin，between，end
        s = list(s)
       
        for i in range(0, len(s), 2*k): # 不要从end角度出发，边界情况会麻烦
            left, right = i, min(i+k-1,len(s)-1)
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                  
        return "".join(s)

# @lc code=end

