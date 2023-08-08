#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
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
    def connect(self, root: 'Node') -> 'Node':
        # 这和1有啥区别,是不是完美二叉树会怎么样？
        if not root: return root
        if not root.left and not root.right: return root

        queue = [root]
        while queue:
            size = len(queue)
            cur = None
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i != 0:
                    cur.next = node
                cur = node
        return root
                
        
# @lc code=end

