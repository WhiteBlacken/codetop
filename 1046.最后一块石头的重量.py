#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        很好奇，这个最后答案是唯一的吗？
        是的，因为每次都选最重
        """
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) >= 2:
            max_1 = heapq.heappop(heap)
            max_2 = heapq.heappop(heap)
            if max_1 == max_2:
                continue
            heapq.heappush(
                heap, (max_1 - max_2) if max_1 - max_2 < 0 else (max_2 - max_1)
            )
        return -heap[0] if len(heap) == 1 else 0


# @lc code=end
