#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        0-1背包
        状态：0和1的剩余量-状态不好建模，三维？
        选择：是否选当前元素
        dp的状态是选择元素的数量
        """
        # 不满足最优子结构啊，首先做个排序
        if m > n: # 则希望1少的在前面
            strs = sorted(strs, key=lambda s: (len(s), s.count('1')))
        else:
            strs = sorted(strs, key=lambda s: (len(s), s.count('0')))
        print(strs)

        m,n,k = len(strs), m, n
        dp = [[[0]*(k+1) for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                for q in range(1,k+1):
                    zero, one = self.get_zero_one(strs[i-1])
                    if j-zero < 0 or q-one < 0:
                        dp[i][j][q] = dp[i-1][j][q]
                    else:
                        dp[i][j][q] = max(
                            dp[i-1][j][q], # 不选
                            dp[i-1][j-zero][q-one] + 1
                        )
        return dp[m][n][k]
    
    def get_zero_one(self, s: str) -> (int, int):
        zero = one = 0
        for ch in s:
            if ch == '0':
                zero += 1
            elif ch == '1':
                one += 1
        return zero, one




# @lc code=end

