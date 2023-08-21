#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(s,tmp):
            if not s:
                res.append(tmp.copy())
                return
            for i in range(len(s)):
                if not self.isPa(s[:i+1]): continue
                tmp.append(s[:i+1])
                backtrack(s[i+1:], tmp)
                tmp.pop()
        backtrack(s, [])

        return res

    def isPa(self, s: str):
        left,right = 0, len(s)-1
        while left < right:
            if s[left]!=s[right]: return False
            left += 1
            right -= 1
        return True
# @lc code=end

