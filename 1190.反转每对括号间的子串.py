#
# @lc app=leetcode.cn id=1190 lang=python3
#
# [1190] 反转每对括号间的子串
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        # 和栈多少有点关系
        stack = []
        item = ""
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(item)
                item = "" # 要清空
                continue
            if s[i] == ')':
                item = stack.pop() + self.reverseStr(item)
                continue
            item += s[i]
        return item

    
    def reverseStr(self, s:str) -> str:
        left, right = 0, len(s) - 1
        s = list(s)
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)


# @lc code=end

