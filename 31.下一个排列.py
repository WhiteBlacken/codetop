#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]: # 非降序时
                for j in range(n-1, i, -1):
                    if nums[j] > nums[i]: # 找到第一个大于nums[i]的数
                        nums[i], nums[j] = nums[j], nums[i]
                        nums[i+1:] = sorted(nums[i+1:])
                        return
        nums.reverse() # 只有这里和下一个排列III返回不一样
# @lc code=end

