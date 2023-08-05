#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        和全排列1的区别：此题包含重复数字
        要求：输出的全排列不重复
        难点：假设有两个1，叫做1a，1b，那按照全排列1中，其实他们对应两种全排列，此题不允许
        解法：固定住顺序，只准a在前，或b在前
        """
        res = []
        nums.sort() # diff
        def backtrack(tmp, visited):
            if len(tmp) ==  len(nums):
                res.append(tmp.copy())
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]: # diff
                    continue 
                visited[i] = True
                tmp.append(nums[i])
                backtrack(tmp, visited)
                tmp.pop()
                visited[i] = False
        backtrack([], [False]*len(nums))
        return res
# @lc code=end

