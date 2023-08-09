#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 二叉树的序列化是否唯一，取决于是否记录null结点
        if not root: return "#"
        # 先序遍历
        return f"{str(root.val)},{self.serialize(root.left)},{self.serialize(root.right)}"

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # 先序遍历逆转
        def helper(queue):
            val = queue.pop(0)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = helper(queue)
            node.right = helper(queue)
            return node
        queue = data.split(",")
        return helper(queue)




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

