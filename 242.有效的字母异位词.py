#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        need = {}
        window = {}
        valid = 0
        for ch in s:
            need[ch] = need.get(ch, 0) + 1
        
        for ch in t:
            if ch in need:
                window[ch] = window.get(ch, 0) + 1
                if window[ch] == need[ch]:
                    valid += 1
        if valid == len(need) and len(s) == len(t):
            return True
        return False

# @lc code=end

