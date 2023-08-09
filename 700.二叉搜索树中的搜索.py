#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        res = None
        def dfs(root):
            nonlocal val, res
            if not root: return root
            if val == root.val:
                res = root
            if val > root.val:
                dfs(root.right)
            else:
                dfs(root.left)
        dfs(root)
        return res

# @lc code=end

