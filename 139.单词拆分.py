#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memx = {}
        def backtrack(s):
            if s in memx: return memx[s]
            if len(s) == 0: return True
            res = False
            for i in range(len(s)):
                if s[:i+1] in wordDict:
                    res = backtrack(s[i+1:]) or res
            memx[s] = res
            return res
        return backtrack(s)
            
# @lc code=end

