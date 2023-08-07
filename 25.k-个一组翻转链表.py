#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
nxt = None
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        a, b = head, head
        for _ in range(k):
            if not b:
                return head
            b = b.next
        new_node = self.reverseNode(a, b)
        a.next = self.reverseKGroup(b, k)
        return new_node

    def reverseNode(self, a, b):
        pre = None
        cur = a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


# @lc code=end

