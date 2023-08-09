#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 建堆的时间复杂度是O(n),最大堆就完事了
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        res = 0
        while k >= 1:
            res = heapq.heappop(heap)
            k -= 1
        return -res


# @lc code=end

