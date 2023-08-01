#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            items = self.twoSum(nums[i+1:], -nums[i])
            res.extend([[nums[i], item[0], item[1]] for item in items])
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res
                

    
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        left, right = 0,len(nums)-1
        res = []
        while left<right:
            tmp = nums[left] + nums[right]
            if tmp == target:
                res.append([nums[left],nums[right]])
                right -= 1
                left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            elif tmp > target:
                right -= 1
            else:
                left += 1
        return res
# @lc code=end

