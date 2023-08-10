#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 二分图可以理解为染色问题：满足相邻结点，颜色不同（共两种颜色，代表两个子集）
        # 那尝试上色吧
        # graph给出的已经是邻接表了
        res = True
        reached = [False]*len(graph)
        color = [False]*len(graph) # 用true和false代表两种颜色
        def backTrack(cur):
            nonlocal res
            if not res: return # 如果已经不是二分图了，返回即可
            reached[cur] = True
            for nxt in graph[cur]:
                if not reached[nxt]: # 没有访问过，上色
                    color[nxt] = not color[cur] # color[cur]在其父节点处已上色
                    backTrack(nxt)
                else:
                    # 从这个相当于替代了return
                    if color[nxt] == color[cur]:
                        res = False
        for i in range(len(graph)):
            backTrack(i) # 不更新reached和color的原因，是不想重复遍历某些节点
            if not res:
                return res
        return True

# @lc code=end

