#
# @lc app=leetcode.cn id=1631 lang=python3
#
# [1631] 最小体力消耗路径
#

# @lc code=start
import queue
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # 乍一看像dp,但是其实不是，因为你不仅要记住前面的最小值，还要知道最小值是怎么来的，因为要做差
        # 也不是最短路径问题，因为他只需要路径的绝对值的最大值，而不是求和
        # 修改迪杰斯特拉的更新条件即可
        m,n = len(heights), len(heights[0])
        graph = self.getGraph(heights)
        disto = self.dijstra(0, graph)
        return disto[m*n-1]

    def dijstra(self, start, graph):
        pq = queue.PriorityQueue()
        disTo = [float('inf')]*len(graph)
        disTo[start] = 0 # 到自己的距离是0
        pq.put(State(start, 0))

        while not pq.empty():
            cur_node = pq.get() # 取出最小的点
            cur_id = cur_node.id
            cur_dist = cur_node.dist

            if cur_dist > disTo[cur_id]:
                continue
            
            for nxt in graph[cur_id]:
                dist = max(cur_dist, nxt[1]) # diff
                if dist < disTo[nxt[0]]:
                    disTo[nxt[0]] = dist
                    pq.put(State(nxt[0], dist))

        return disTo

    def getGraph(self, heights):
        m, n = len(heights), len(heights[0])
        graph = [[] for _ in range(m*n)]
        min_idx, max_idx = 0, m*n-1
        for i in range(m):
            for j in range(n):
                idx = i*n + j
                nxts = [(i-1)*n + j,(i+1)*n + j, i*n + j - 1, i*n + j + 1]
                for nxt in nxts:
                    if nxt < min_idx or nxt > max_idx:
                        continue
                    cur_i, cur_j = nxt//n, nxt%n
                    graph[idx].append((nxt, abs(heights[cur_i][cur_j]-heights[i][j])))

        return graph

class State:
    def __init__(self, id, dist) -> None:
        self.id = id
        self.dist = dist
    
    def __lt__(self, other):
        return self.dist < other.dist
        
# @lc code=end

