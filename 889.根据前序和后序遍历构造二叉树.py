#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
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
        self.preIndex = 0
        self.postIndex = 0
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 前序和中序无法唯一的确定二叉树
        # 那怎么确定一个合理的树，满足要求呢？
        root = TreeNode(preorder[self.preIndex])
        self.preIndex += 1
        if root.val != postorder[self.postIndex]:
            root.left = self.constructFromPrePost(preorder, postorder)
        if root.val != postorder[self.postIndex]:
            root.right = self.constructFromPrePost(preorder, postorder)
        
        self.postIndex += 1
        return root

# @lc code=end

