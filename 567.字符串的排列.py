#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        need = {}
        window = {}
        valid = 0 # 关键先生
        left = 0
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1
        
        for right in range(len(s2)):
            ch = s2[right]
            if ch in need:
                window[ch] = window.get(ch, 0) + 1
                if window[ch] == need[ch]:
                    valid += 1
            while valid == len(need): # 开始缩小空间
                if right - left + 1 == len(s1):
                    return True
                ch = s2[left]
                left += 1
                if ch in need:
                    if window[ch] == need[ch]:
                        valid -= 1
                    window[ch] -= 1

        return False
        

# @lc code=end

