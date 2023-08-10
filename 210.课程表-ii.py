#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # bfs-拓扑-环判断
        # 如果入度为0，则说明不需要前置知识
        # 邻接表
        matrix = self.getMatrix(numCourses, prerequisites)
        indegree = [0]*numCourses
        for pere in prerequisites:
            indegree[pere[0]] += 1
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        res = []
        while queue: # 在queue里的都是没有前置知识的
            node = queue.pop(0)
            res.append(node)
            for item in matrix[node]:
                indegree[item] -= 1
                if indegree[item] == 0:
                    queue.append(item)
        if len(res) != numCourses:
            return []
        return res

    def findOrder_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # dfs
        # 拓扑排序-图的后序遍历
        # 在后序遍历过程中，判断是否有环，有环的话，无结果
        # 1. 构建邻接表
        matrix = self.getMatrix(numCourses, prerequisites)
        # 2. 深度遍历
        onPath = [False]*numCourses
        visited = [False]*numCourses
        postOrder = []
        hasCircle = False
        def backtrack(cur):
            nonlocal hasCircle
            if hasCircle or onPath[cur]:
                hasCircle = True
                return
            if visited[cur]: return
            visited[cur] = True
            onPath[cur] = True
            for item in matrix[cur]: # 子节点们
                backtrack(item)
            onPath[cur] = False
            postOrder.append(cur)
        
        for i in range(numCourses):
            backtrack(i)
        if hasCircle:
            return []
        postOrder.reverse()
        return postOrder
    
    def getMatrix(self, numCourses: int, prerequisites: List[List[int]]) -> List[List[int]]:
        matrix = [[] for _ in range(numCourses)]
        for pere in prerequisites:
            matrix[pere[1]].append(pere[0])
        return matrix

    



# @lc code=end

