#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 划重点：只能使用一次，但是集合中会有重复（没明说），输出不能重复
        # 组合问题使用visited来记录，子集问题不需要
        res = []
        candidates.sort()
        def backtrack(start, tmp):
            if sum(tmp) == target:
                res.append(tmp.copy())
                return
            if sum(tmp) > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]: # diff
                    continue
                tmp.append(candidates[i])
                backtrack(i+1, tmp) # 到了下一层，相同也无所谓了
                tmp.pop()
        backtrack(0, [])
        return res
# @lc code=end

