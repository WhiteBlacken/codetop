#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 先序+中序简单
        # 还是不断拆解子问题
        if len(preorder) == 0: return None
        num = preorder.pop(0)
        split = inorder.index(num)
        root = TreeNode(num)
        root.left = self.buildTree(preorder[:split],inorder[:split])
        root.right = self.buildTree(preorder[split:],inorder[split+1:])
        return root

# @lc code=end

