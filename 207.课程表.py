#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 解法二：bfs
        # 如果能够把前置全部学完，最后能够所有课程学完，即无环->入度
        matrix = self.getGraph(numCourses, prerequisites)
        indegree = [0]*numCourses
        for pere in prerequisites:
            indegree[pere[0]] += 1
        queue = [i for i, num in enumerate(indegree) if num == 0]
        cnt = 0
        while queue:
            node = queue.pop(0) # pop就是学了
            cnt += 1
            # 邻接表中对应的入度都-1
            for i in matrix[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        return cnt == numCourses  # 说明所有的课程都学完了
    
    def canFinish_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 解法一：dfs
        # 先翻译成图的邻接表或者邻接矩阵，再检测是否成环
        # 也用遍历的想法来，判断是否会访问到visited为True的结点
        matrix = [[] for _ in range(numCourses)]
        for pere in prerequisites:
            matrix[pere[1]].append(pere[0])
        onpath = [False]*numCourses
        reached = [False]*numCourses # 只要用于剪枝
        hasCircle = False
        def backtrack(cur, onpath):
            nonlocal hasCircle
            if onpath[cur] or hasCircle:
                hasCircle = True
                return 
            if reached[cur]: return
            onpath[cur] = True
            reached[cur] = True
            for item in matrix[cur]:
                backtrack(item, onpath)
            onpath[cur] = False
        for i in range(numCourses):
            backtrack(i, onpath)
            if hasCircle:
                return False
        return True
    
    def getGraph(self, numCourses, prerequisites):
        matrix = [[] for _ in range(numCourses)]
        for pere in prerequisites:
            matrix[pere[1]].append(pere[0])
        return matrix

# @lc code=end

