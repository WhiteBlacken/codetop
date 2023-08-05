#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deads = set(deadends)
        q1, q2 = set(), set()
        visited = set()
        step = 0

        q1.add('0000')
        q2.add(target)

        while q1 and q2:
            tmp = set()
            for cur in q1:
                if cur in deads:
                    continue

                if cur in q2:
                    return step
                
                visited.add(cur)

                for j in range(4):
                    up = self.plusOne(cur, j)
                    if up not in visited:
                        tmp.add(up)
                    down = self.minorOne(cur, j)
                    if down not in visited:
                        tmp.add(down)
            step += 1
            q1, q2 = q2, tmp
        return -1


    def minorOne(self, node, j):
        res = [int(item) for item in node]
        res[j] = (res[j] - 1)%10
        return "".join(map(str, res))

    def plusOne(self, node, j):
        res = [int(item) for item in node]
        res[j] = (res[j] + 1)%10
        return "".join(map(str, res))
# @lc code=end

