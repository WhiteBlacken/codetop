#
# @lc app=leetcode.cn id=556 lang=python3
#
# [556] 下一个更大元素 III
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # 这个和base版的下一个更大元素已经没关系了
        # 和 下一个屁啊列 是同一题
        """
        从右往左遍历，找到第一个不是降序的，从后找到最小值且比当前值大的交换,然后排序
        """
        nums = []
        while n > 0:
            nums.append(n%10)
            n //= 10
        nums.reverse()
        n = len(nums)
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                # 处理逻辑
                for j in range(n-1, i, -1): # 因为是递减的
                    if nums[j] > nums[i]:
                        # 交换
                        nums[i], nums[j] = nums[j], nums[i]
                        nums[i+1:] = sorted(nums[i+1:])
                        val = self.arrayToNums(nums)
                        return val if val <= 2**31 - 1 else -1
        return -1
    
    def arrayToNums(self, nums):
        val = 0
        mul = 1
        while nums:
            val += nums.pop()*mul
            mul *= 10
        return val

          

# @lc code=end

