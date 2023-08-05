#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(tmp, visited):
            if len(tmp) == len(nums):
                res.append(tmp.copy())
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                tmp.append(nums[i])
                visited[i] = True
                backtrack(tmp, visited)
                visited[i] = False
                tmp.pop()

        backtrack([], [False]*len(nums))
        return res
            

# @lc code=end

