#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 划重点：无重复元素，可多次使用，返回的所有结果
        # 如果只问组合数？->考虑dp，零钱兑换II

        # 如果得到所有子集怎么做？-> 不是排列，不用回头
        res = []
        def backtrack(start, tmp):
            if sum(tmp) == target:
                res.append(tmp.copy())
                return
            if sum(tmp) > target: # 如果这里没有剪枝，会无限循环下去
                return
            
            for i in range(start, len(candidates)):
                tmp.append(candidates[i])
                backtrack(i, tmp) # 因为元素可以无限使用，所以不用+1
                tmp.pop()
        backtrack(0, [])
        return res
                
            
# @lc code=end

