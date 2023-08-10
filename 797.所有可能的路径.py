#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # 感觉就是个回溯啊
        n = len(graph)
        res = []
        # 不包含环，不需要visited
        def backtrack(cur, tmp):
            if cur == n-1:
                tmp.append(cur)
                res.append(tmp.copy())
                tmp.pop()
                return 
            
            tmp.append(cur)
            for item in graph[cur]:
                backtrack(item, tmp)
            tmp.pop()

        backtrack(0, [])
        return res

# @lc code=end

