#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.node = None

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        self.searhBST(root, val)
        if val > self.node.val:
            self.node.right = TreeNode(val)
        else:
            self.node.left = TreeNode(val)
        return root

    def searhBST(self, root, val):
        if not root: return
        self.node = root
        if val > root.val:
            self.searhBST(root.right, val)
        else:
            self.searhBST(root.left, val)

# @lc code=end

