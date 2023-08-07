#
# @lc app=leetcode.cn id=1674 lang=python3
#
# [1674] 使数组互补的最少操作次数
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        # 数对的范围：[2, 2*limit],多开点没事，省的坐标偏移了
        n = len(nums)
        mid = len(nums) // 2
        diff = [0]*(2*limit+2)
        for i in range(mid):
            a,b = nums[i], nums[n-i-1]
            sum_val,min_val,max_val = a+b, min(a,b), max(a,b)
            """
            操作分为3种:
            操作0次:sum_val
            操作1次:[sum_val-max_val+1,sum_val),(sum_val, sum_val+limit-min_val]
            操作2次:[2,sum_val-max_val+1),(sum_val+limit-min_val,2*limit]
            """
            if sum_val-max_val+1 < sum_val: 
                diff[sum_val-max_val+1] += 1
                diff[sum_val] -= 1
            if sum_val < sum_val+limit-min_val:
                diff[sum_val+1] += 1
                diff[sum_val+limit-min_val+1] -= 1
            if sum_val - max_val > 1:
                diff[2] += 2
                diff[sum_val-max_val+1] -= 2
            if sum_val+limit-min_val < 2*limit:
                diff[sum_val+limit-min_val+1] += 2
                diff[2*limit+1] -= 2
        res = float('inf')
        for i in range(2, 2*limit+1):
            diff[i] += diff[i-1]
            res = min(diff[i], res)
        return res



# @lc code=end

