#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # 这不是层序遍历就行了
        if not root: return root
        if not root.left and not root.right: return root
        queue = [root]
        cur = root
        while queue:  
            size = len(queue)
            cur = None
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == 0:
                    cur = node
                else:
                    cur.next = node
                    cur = cur.next
        return root
        

# @lc code=end

