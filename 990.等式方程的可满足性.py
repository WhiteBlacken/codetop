#
# @lc app=leetcode.cn id=990 lang=python3
#
# [990] 等式方程的可满足性
#

# @lc code=start
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        class UF:
            def __init__(self, n) -> None:
                self.parent = list(range(n)) # 指向自己
                self.size = [1]*n # 每个树都仅有自己这个节点，为了平衡引入该变量
            
            def find(self, x):
                # 在find里做了修改操作，其实不该出现在这
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x]) # 将其父节点设为其祖父节点
                return self.parent[x]
            
            def union(self, x, y): # 这里可以计算连通分量
                root_x, root_y = self.find(x), self.find(y)
                if root_x == root_y: return
                if self.size[root_x] < self.size[root_y]:
                    root_x, root_y = root_y, root_x
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            
            def connected(self, x, y):
                return self.find(x) == self.find(y)
        uf = UF(26)
        for eq in equations:
            if eq[1] == '=':
                x, y = eq[0], eq[3]
                uf.union(ord(x)-ord('a'), ord(y)-ord('a'))
        for eq in equations:
            if eq[1] == '!':
                x, y = eq[0], eq[3]
                if uf.connected(ord(x)-ord('a'),ord(y)-ord('a')):
                    return False
        return True

# @lc code=end

