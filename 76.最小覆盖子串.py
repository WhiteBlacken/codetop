#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 重要是怎么知道是否满足的要求？
        need = {} 
        window = {}
        valid = 0 # 这个是关键
        left = 0
        length = float('inf')
        start = 0
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        
        for right in range(len(s)):
            c = s[right]
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need): # 只要符合要求，就可以一直收缩
                if right - left + 1 < length:
                    start, length = left, right - left + 1
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return "" if length == float('inf') else s[start: start+length]



# @lc code=end

