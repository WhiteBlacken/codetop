#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#

# @lc code=start
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # 二分图的实际应用
        # 两组，dislikes代表了节点关系，最后希望相邻节点不同色
        # 首先要把题目条件翻译成邻接表/邻接矩阵
        res = True
        graph = self.getGraph(n, dislikes)
        reached = [False]*n
        color = [False]*n
        def backtrack(cur):
            nonlocal res
            if not res: return # 剪个枝
            reached[cur] = True
            for nxt in graph[cur]:
                if reached[nxt]: # 该节点已经被访问过了
                    if color[nxt] == color[cur]:
                        res = False
                else:
                    color[nxt] = not color[cur]
                    backtrack(nxt)
        for i in range(n):
            backtrack(i)
            if not res:
                return False
        return True

    def getGraph(self, n, dislikes):
        graph = [[] for _ in range(n)]
        for dislike in dislikes: # 题目编号从1开始，处理下
            graph[dislike[0]-1].append(dislike[1]-1)
            graph[dislike[1]-1].append(dislike[0]-1)
        return graph


# @lc code=end

