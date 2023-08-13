#
# @lc app=leetcode.cn id=496 lang=python
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = len(nums2)
        res = [0 for _ in range(n)]
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(nums2[i])
        # 写入dict
        dict = {num: res[i] for i, num in enumerate(nums2)}
        return [dict[num] for num in nums1]

# @lc code=end

