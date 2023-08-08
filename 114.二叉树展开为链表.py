#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None, None
        if not root.left and not root.right: return root, root
        if root.left and root.right:
            l_start, l_end = self.flatten(root.left)
            r_start, r_end = self.flatten(root.right)
            root.right = l_start
            root.left = None
            l_end.right = r_start
            l_end.left = None
        elif root.right:
            r_start, r_end = self.flatten(root.right)
            root.right = r_start
            root.left = None
        elif root.left:
            l_start, l_end = self.flatten(root.left)
            root.right = l_start
            root.left = None
            return root, l_end

        return root, r_end
# @lc code=end

