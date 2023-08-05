#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        尝试所有情况，每步两种选择，大写或小写
        不是全排列，只用回头一步，不用从头开始选
        """
        res = []
        def backtrack(start, tmp):
            if len(tmp) == len(s):
                res.append("".join(tmp.copy()))
                return
            for i in range(start, len(s)):
                if not s[i].isalpha():
                    tmp.append(s[i])
                    backtrack(i+1, tmp)
                    tmp.pop() # 这里不弹出，后面弹出了也没用
                    continue

                tmp.append(s[i].lower())
                backtrack(i+1, tmp)
                tmp.pop()

                tmp.append(s[i].upper())
                backtrack(i+1, tmp)
                tmp.pop()
        backtrack(0, [])
        return res
            
# @lc code=end

