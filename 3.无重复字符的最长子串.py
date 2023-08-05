#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        left = win = 0
        chat_index = {} # 记录位置，这个最关键
        for right in range(len(s)):
            while s[right] in chat_index and chat_index[s[right]] >= left:
                left = chat_index[s[right]] + 1
            win = max(win, right-left+1)
            chat_index[s[right]] = right
        return win






# @lc code=end

