#
# @lc app=leetcode.cn id=1094 lang=python3
#
# [1094] 拼车
#

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 主要关心的是每一位上的值，是否有超过capcity的
        # 因为区间可能有重叠，会对一个较长的区间反复增（删，无删）
        # 差分数组：频繁对区间增删
        diff = [0]*1001
        for trip in trips:
            diff[trip[1]] += trip[0]
            diff[trip[2]] -= trip[0]
        
        for i in range(len(diff)):
            if i > 0:
                diff[i] += diff[i-1]
            if diff[i] > capacity:
                return False
        return True

# @lc code=end

