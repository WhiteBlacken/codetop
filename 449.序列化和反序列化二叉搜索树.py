#
# @lc app=leetcode.cn id=449 lang=python3
#
# [449] 序列化和反序列化二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        # 如果不考虑他是二叉搜索树，直接按照二叉树来序列化
        # 但是要求尽可能紧凑了
        if not root: return '#'
        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        def helper(queue): # 先序遍历逆向
            node = queue.pop(0)
            if node == '#': return None
            node = TreeNode(int(node))
            node.left = helper(queue)
            node.right = helper(queue)
            return node
        queue = data.split(",")
        return helper(queue)

        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end

