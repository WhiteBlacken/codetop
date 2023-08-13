#
# @lc app=leetcode.cn id=743 lang=python3
#
# [743] 网络延迟时间
#

# @lc code=start
import queue
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 算单源最短距离的最大值
        # 以及连通性 -正无穷就是不连通呗
        graph = [[] for _ in range(n+1)]
        for begin, end, weight in times:
            graph[begin].append((end, weight))
        disTo = self.dijkstra(k, graph)
        res = 0
        for i, dist in enumerate(disTo):
            if i == 0: continue
            if dist == float('inf'):
                return -1
            res = max(res, dist)
        return res
    
    def dijkstra(self, start: int, graph: List[List[int]]) -> List[int]:
        dist_to = [float('inf')]*len(graph)
        dist_to[start] = 0 # base case
        pq = queue.PriorityQueue()
        pq.put(State(start, 0))

        while not pq.empty():
            cur_state = pq.get() # 选中这个点，更新其所有邻接点
            cur_node = cur_state.id
            cur_dist = cur_state.dist

            if cur_dist > dist_to[cur_node]:
                continue

            for nxt in graph[cur_node]:
                nxt_id = nxt[0]
                dist = dist_to[cur_node] + nxt[1]
                if dist_to[nxt_id] > dist:
                    dist_to[nxt_id] = dist
                    pq.put(State(nxt_id, dist)) # 最新的结果都存进pq了
                    # 有重复的结点，这时上面的continue就生效了
        return dist_to

class State:
    def __init__(self, id, dist) -> None:
        self.id = id
        self.dist = dist
    
    def __lt__(self, other):
        return self.dist < other.dist
# @lc code=end

