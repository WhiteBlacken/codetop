#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 完全二叉树的子树，包含满二叉树
        l = r = root
        hl = hr = 0
        while l:
            l = l.left
            hl += 1
        while r:
            r = r.right
            hr += 1
        if hl == hr:
            return pow(2, hl) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
       
    def countNodes_1(self, root: Optional[TreeNode]) -> int:
        # 暴力解也能过，没有利用完全二叉树的性质
        if not root: return 0
        queue = [root]
        res = 0
        while queue:
            size = len(queue)
            res += size
            for _ in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
            
# @lc code=end

