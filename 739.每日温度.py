#
# @lc app=leetcode.cn id=739 lang=python
#
# [739] 每日温度
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # 看后面第一个最大的：单调栈
        n = len(temperatures)
        res = [0 for _ in range(n)]
        stack = []
        for i in range(n-1,-1,-1):
            while stack and temperatures[stack[-1]] <= temperatures[i]: # 记录的是下标
                stack.pop()
            res[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return res
# @lc code=end

