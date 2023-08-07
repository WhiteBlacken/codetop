#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        self.prefix.extend(self.prefix[-1]+item for item in nums)


    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left] # 数组实际向右偏移1位



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

