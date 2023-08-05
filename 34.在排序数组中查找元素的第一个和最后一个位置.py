#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        二分查找呗
        """
        return [self.left_bound(nums, target), self.right_bound(nums, target)]
    
    def left_bound(self, nums: list, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1 if left >= len(nums) or nums[left] != target else left # diff

    def right_bound(self, nums: list, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        print(right)
        return -1 if right <0 or nums[right] != target else right # diff

# @lc code=end

