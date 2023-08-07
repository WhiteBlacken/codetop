#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#

# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 差分数组：对区间反复增删
        diff = [0]*(2*10**4+1)
        for start,end,seat in bookings:
            diff[start-1] += seat
            diff[end] -= seat
        for i in range(1, len(diff)):
            diff[i] += diff[i-1]
        return diff[:n]

# @lc code=end

