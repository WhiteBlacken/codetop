#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0: return None
        # 后序就反过来处理
        num = postorder.pop()
        split = inorder.index(num)
        # 中序总是很好处理
        root = TreeNode(num)
        root.left = self.buildTree(inorder[:split], postorder[:split]) # post从末尾pop的，好处理
        root.right = self.buildTree(inorder[split+1:], postorder[split:])
        return root
# @lc code=end

