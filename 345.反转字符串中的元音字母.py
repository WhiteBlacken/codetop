#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        # 左右指针，就多了个原因字母的判断
        left, right = 0, len(s)-1
        rep_list = ['a','e','i','o','u','A','E','I','O','U']
        # 字符串无法原地旋转，所以返回str
        s = list(s)
        while left < right:
            while left < right and s[left] not in rep_list:
                left += 1
            while left  < right and s[right] not in rep_list:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)
            
# @lc code=end

