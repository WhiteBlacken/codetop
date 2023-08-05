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
        m,n,k = len(strs), m, n
        dp = [[[0]*(k+1) for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                for q in range(k+1):
                    if i == 0:
                        dp[i][j][q] = 0
                        continue
                    if j == 0 and q == 0:
                        dp[i][j][q] = 0
                        continue
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

