/*
 * @lc app=leetcode.cn id=445 lang=java
 *
 * [445] 两数相加 II
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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode l1_r = reverse(l1), l2_r = reverse(l2);
        ListNode dummy = new ListNode(-1), cur=dummy;
        int carry = 0;
        while(l1_r!=null||l2_r!=null||carry!=0){
            int a = (l1_r==null)? 0:l1_r.val;
            int b = (l2_r==null)? 0:l2_r.val;
            cur.next = new ListNode((a+b+carry)%10);
            cur = cur.next;
            carry = (a+b+carry)/10;
            l1_r = (l1_r==null)? l1_r:l1_r.next;
            l2_r = (l2_r==null)? l2_r:l2_r.next;
        }
        return reverse(dummy.next);

    }
    public ListNode reverse(ListNode head){
        ListNode pre = null;
        while(head!=null){
            ListNode nxt_node = head.next;
            head.next = pre;
            pre = head;
            head = nxt_node;
        }
        return pre;
    }
}
// @lc code=end

