#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root
        if root.val == key:
            # 删除
            # 无子结点或单结点的情况
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # 用右子树的最小结点或左子树的最小结点
            minNode = self.getMin(root.right)
            root.right = self.deleteNode(root.right, minNode.val) # 一致迭代删除下去
            minNode.left = root.left
            minNode.right = root.right
            root = minNode
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def getMin(self, node):
        while node.left:
            node = node.left
        return node
# @lc code=end

