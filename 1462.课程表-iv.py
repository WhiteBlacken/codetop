#
# @lc app=leetcode.cn id=1462 lang=python3
#
# [1462] 课程表 IV
#

# @lc code=start
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # 这题做起来和之前的差不多，都是有向图的遍历；
        # 本题默认无环
        # 主要是处理这个query的问题
        """
        1. 是否可以转成，如果把query拿掉，另一个的入度会不会减少？未必，可能有其他条件
        2. 转换成遍历问题，看是否从query出发，能遍历到另一个？
        """
        graph = self.getGraph(numCourses, prerequisites)
        res = []
        for query in queries:
            visited = [False]*numCourses
            reached = [False]*numCourses
            self.backtrack(query[0], graph, visited, reached)
            if reached[query[1]]:
                res.append(True)
            else:
                res.append(False)
        return res

    def backtrack(self, cur, graph, visited, reached):
        if reached[cur]: return # 如果这个点到过了，即所有可能的情况都已经被遍历了
        reached[cur] = True # 记录来过了
        visited[cur] = True
        for nxt in graph[cur]:
            self.backtrack(nxt, graph, visited, reached)
        visited[cur] = False


    def getGraph(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for pere in prerequisites: # a是b的前置，与其他课程表问题是反的
            graph[pere[0]].append(pere[1])
        return graph

# @lc code=end

