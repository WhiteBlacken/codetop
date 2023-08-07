#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 回文链表？链表不能回头
        # 直接反转链表的话，也会改变原链表
        # 反转一半
        if not head or not head.next: return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = self.reverseNode(slow)
      
        while mid and head:
            if mid.val != head.val:
                return False
            mid = mid.next
            head = head.next
        return True

        

    def reverseNode(self, head):
        if not head or not head.next: return head
        pre = self.reverseNode(head.next)
        head.next.next = head
        head.next = None
        return pre
# @lc code=end

