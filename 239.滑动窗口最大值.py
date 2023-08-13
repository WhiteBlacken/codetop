#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        qu = MonotionQueue()
        for i in range(k):
            qu.push(nums[i])
        res.append(qu.max())
        left, right = 0, k-1
        while right < len(nums) - 1:
            # 删去左结点
            qu.pop(nums[left])
            left += 1
            # 添加右结点
            right += 1
            qu.push(nums[right])
            res.append(qu.max())
        return res
        
class MonotionQueue:
    def __init__(self) -> None:
        self.maxq = []
    
    def push(self, n):
        while self.maxq and self.maxq[-1] < n:
            self.maxq.pop()
        self.maxq.append(n) # 和单调队列一样，不过就是支持双头
    
    def max(self):
        return self.maxq[0]
    
    def pop(self, n):
        if n == self.maxq[0]: # 在当前场景下每次弹出的都是队头
            self.maxq.pop(0)
        
# @lc code=end

