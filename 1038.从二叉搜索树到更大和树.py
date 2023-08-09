#
# @lc app=leetcode.cn id=1038 lang=python3
#
# [1038] 从二叉搜索树到更大和树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 直接调个顺序遍历一遍
        res = [0]
        def dfs(root):
            if not root: return
            dfs(root.right)
            root.val += res[0]
            res[0] = max(res[0], root.val)
            dfs(root.left)
        dfs(root)
        return root
            
        
# @lc code=end

