#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []
        res = []
        need = {}
        window = {}
        valid = 0
        left = 0
        for ch in p:
            need[ch] = need.get(ch, 0) + 1
        for right in range(len(s)):
            ch = s[right]
            if ch in need:
                window[ch] = window.get(ch, 0) + 1
                if window[ch] == need[ch]:
                    valid += 1
            while valid == len(need): 
                if right - left + 1 == len(p):
                    res.append(left)
                ch = s[left]
                left += 1
                if ch in need:
                    if window[ch] == need[ch]:
                        valid -= 1
                    window[ch] -= 1
        return res

 
# @lc code=end

