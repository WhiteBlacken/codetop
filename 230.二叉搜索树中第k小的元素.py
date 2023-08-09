#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 应该自底向上遍历
        # 离开结点时计算
        class Found(Exception):
            pass

        res = [0]
        def dfs(root):
            nonlocal k
            if not root: return
            dfs(root.left)
            if k == 1: 
                res[0] = root.val
                raise Found()
            k -= 1 # 离开结点去右子树了
            dfs(root.right)
        try:
            dfs(root)
        except Found:
            pass
        return res[0]



# @lc code=end

