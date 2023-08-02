/*
 * @lc app=leetcode.cn id=83 lang=java
 *
 * [83] 删除排序链表中的重复元素
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        //和删除重复数组类似，操作上不同，主要是数组可以通过下标访问
        if(head==null)return head;
        ListNode dummy = new ListNode(-1),cur = dummy;
        while(head!=null){
            while(head!=null&&head.next!=null&&head.val==head.next.val)head=head.next;
            cur.next = head;
            cur = cur.next;
            head = head.next;
        }
        return dummy.next;
    }
}
// @lc code=end

