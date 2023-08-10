#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 和海洋陆地的题很像，先沿着边做dfs，标记下
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if (i*j == 0 or i == m-1 or j == n-1) and board[i][j] == 'O':
                    self.dfs(board, i, j, 'Z')
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    self.dfs(board, i, j, 'X')
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'Z':
                    board[i][j] = 'O'
    
    def dfs(self, board, i, j, val):
        m, n = len(board), len(board[0])
        if i < 0 or j < 0 or i >= m or j >= n: 
            return
        if board[i][j] != 'O':
            return
        board[i][j] = val
        self.dfs(board, i-1, j, val)
        self.dfs(board, i+1, j, val)
        self.dfs(board, i, j-1, val)
        self.dfs(board, i, j+1, val)

# @lc code=end

