#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.strip().split(" ")
        res = [item for item in res if len(item.strip())>0]
        res.reverse()
        return " ".join(res)
# @lc code=end

