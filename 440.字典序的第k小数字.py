#
# @lc app=leetcode.cn id=440 lang=python3
#
# [440] 字典序的第K小数字
#

# @lc code=start
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # 这个放到堆里也行，要自定义大小比较
        def countNumbers(prefix, n):
            cur = prefix
            next = prefix + 1
            count = 0
            while cur < n:
                count += min(n+1, next) - cur
                cur *= 10
                next *= 10
            return next
        cur = 1
        k -= 1
        while k > 0:
            count = countNumbers(cur, n)
            if count <= k:
                cur += 1
                k -= count
            else:
                cur * 10
                k -= 1
        return cur
        
# @lc code=end

