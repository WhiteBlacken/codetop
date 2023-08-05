#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N 皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        def backtrack(row, tmp, visited):
            if row == n: # n行均以遍历完
                ans = []
                for item in tmp:
                    ans.append(answer_format(item))
                res.append(ans)
                return
            for i in range(n): # 遍历n列
                # 确定剪枝条件
                if visited[row][i] > 0:
                    continue

                tmp.append(i)
                set_val(row, i, visited, 1)
                backtrack(row+1, tmp, visited)
                set_val(row, i, visited, -1)
                tmp.pop()

        def set_val(i, j, visited, val):
            for col in range(n):
                visited[i][col] += val
            for row in range(n):
                visited[row][j] += val
            
            visited[i][j] -= val # 多计算了一次
            m1,n1 = i-1,j-1 # 左上
            while m1 >= 0 and n1 >= 0:
                visited[m1][n1] += val
                m1 -= 1
                n1 -= 1
            m1,n1 = i+1,j+1 # 右下
            while m1 < n and n1 < n:
                visited[m1][n1] += val
                m1 += 1
                n1 += 1
            m1,n1 = i+1,j-1 # 左下
            while m1 < n and n1 >= 0:
                visited[m1][n1] += val
                m1 += 1
                n1 -= 1
            m1,n1 = i-1,j+1 # 右上
            while m1 >= 0 and n1 < n:
                visited[m1][n1] += val
                m1 -= 1
                n1 += 1
        def answer_format(i):
            ans = ["."]*n
            ans[i] = "Q"
            return "".join(ans)
        
        backtrack(0, [], [[0]*n for _ in range(n)])
        

        return len(res)
# @lc code=end

