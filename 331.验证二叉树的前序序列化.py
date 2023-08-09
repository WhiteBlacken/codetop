#
# @lc app=leetcode.cn id=331 lang=python3
#
# [331] 验证二叉树的前序序列化
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # 序列化的方法与我之前的写的一致
        # 用栈挺绝的
        # 每两个子节点消耗一个父结点
        stack = []
        preorder = preorder.split(",")
        for item in preorder:
            tmp = item
            while tmp == '#' and stack and stack[-1] == '#':
                for _ in range(2):
                    if not stack: return False
                    stack.pop()
                tmp = '#'
            stack.append(tmp)
        return len(stack) == 1 and stack[0] == '#'






# @lc code=end

