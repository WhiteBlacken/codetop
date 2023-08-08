#
# @lc app=leetcode.cn id=710 lang=python3
#
# [710] 黑名单中的随机数
#

# @lc code=start
import random
class Solution:
    # 拒绝采样，但是会调用很多次
    # 如何优化
    def __init__(self, n: int, blacklist: List[int]):
        self.size = n - len(blacklist)
        self.dict = {}
        for b in blacklist:
            self.dict[b] = 666
        
        last = n - 1
        for b in blacklist:
            if b >= self.size:
                continue
            while last in self.dict:
                last -= 1
            self.dict[b] = last
            last -= 1


    def pick(self) -> int:
        num = random.randint(0, self.size-1)
        if num in self.dict:
            return self.dict[num]
        return num



# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
# @lc code=end

