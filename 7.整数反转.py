#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # 先把符号记一下？然后反转呗
        # 有个问题：反转后如果超出范围怎么办？
        sig = 1 if x >= 0 else -1
        res = [] # 实际上是个常数大小
        x = x if x >= 0 else -x
        while x>0:
            res.append(x%10)
            x //= 10
        mul = 1
        num = 0
        for i in range(len(res)-1,-1,-1):
            num += res[i]*mul
            mul *= 10
        if sig == 1 and num > 2**31 - 1: return 0 # python里可以这么干，其他的里就算了
        if sig == -1 and num > 2**31: return 0
        
        return sig*num
        

# @lc code=end

