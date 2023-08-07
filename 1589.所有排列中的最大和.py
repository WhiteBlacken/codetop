#
# @lc app=leetcode.cn id=1589 lang=python3
#
# [1589] 所有排列中的最大和
#

# @lc code=start
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # 按照查询次数，排序，查询次数最多的位置放最大的值
        # 最后只要输出结果就行
        diff = [0]*(10**5+1)
        for start, end in requests:
            diff[start] += 1
            diff[end+1] -= 1
        for i in range(1, len(diff)):
            diff[i] += diff[i-1]
        diff.sort(reverse=True) # 按查询排序
        nums.sort(reverse=True)

        return sum(nums[i]*diff[i] for i in range(len(nums)))%(10**9+7)



# @lc code=end

