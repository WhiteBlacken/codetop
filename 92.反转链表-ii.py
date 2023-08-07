#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 记下三个位置，before，node，after
        # 能做但很蠢
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while left > 1:
            cur = cur.next
            left -= 1
        before = cur # 1
        node = before.next # 2

        cur = dummy
        while right > 0:
            cur = cur.next
            right -= 1
        after = cur.next # 3 
        cur.next = None

        root = self.reverseList(node)
        before.next = root

        while root and root.next:
            root = root.next
        root.next = after
        return dummy.next
    
    def reverseList(self, root):
        if not root or not root.next: return root
        pre = self.reverseList(root.next)
        root.next.next = root
        root.next = None
        return pre

# @lc code=end

