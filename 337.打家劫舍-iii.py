#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # 离谱，升级到了二叉树版本

        def dfs(root):
            if not root:
                return 0,0
            l, l_not = dfs(root.left)
            r, r_not = dfs(root.right)

            rob = l_not + r_not + root.val
            not_rob = max(l, l_not) + max(r, r_not)
            return rob, not_rob
        return max(dfs(root))
# @lc code=end

