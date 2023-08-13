#
# @lc app=leetcode.cn id=503 lang=python
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 环型
        # 两个数组拼接就可以，但是可以只模拟。用求余才替代
        n = len(nums)
        res = [-1]*n
        stack = []
        for i in range(2*n-1,-1,-1):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            res[i%n] = stack[-1] if stack else -1
            stack.append(nums[i%n])
        return res
# @lc code=end

