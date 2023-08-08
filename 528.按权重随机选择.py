#
# @lc app=leetcode.cn id=528 lang=python3
#
# [528] 按权重随机选择
#

# @lc code=start
import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = [w[0]]
        # 数组不变了，可以前缀和
        for i in range(1, len(w)):
            self.w.append(self.w[-1] + w[i])

    def pickIndex(self) -> int:
        # 范围是[1, self.w[-1]]
        pick = random.randint(1, self.w[-1])
        left, right = 0, len(self.w) - 1
        while left < right: # 要找的接近的靠右的数,这种二分怎么查
            mid = left + (right-left) // 2
            if self.w[mid] == pick:
                return mid # 返回的是下标
            if self.w[mid] > pick:
                right = mid
            else:
                left = mid + 1
        return right







# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

