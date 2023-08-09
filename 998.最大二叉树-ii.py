#
# @lc app=leetcode.cn id=998 lang=python
#
# [998] 最大二叉树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # 其实就是插入一个树，但是不改变最大树本身的性质
        # 这题出的不好，题意不清楚
        if not root: # 到了根节点，直接插入进行
            return TreeNode(val)
        if root.val < val:
            node = TreeNode(val)
            node.left = root
            return node
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
    
# @lc code=end

