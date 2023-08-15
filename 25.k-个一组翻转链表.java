/*
 * @lc app=leetcode.cn id=25 lang=java
 *
 * [25] K 个一组翻转链表
 */

// @lc code=start

import javax.swing.plaf.TreeUI;

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
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode a,b;
        a = b = head;
        for(int i=0;i<k;i++){
            if(b==null)return head; //不反转
            b = b.next;
        }
        ListNode newNode = reverse(a, b);
        a.next = reverseKGroup(b, k);
        return newNode;
    }
    ListNode reverse(ListNode a, ListNode b){
        ListNode pre, cur, nxt;
        pre = null; cur = a;
        while(cur!=b){
            nxt = cur.next;
            cur.next = pre;
            pre = cur;
            cur = nxt;
        }
        return pre;
    }
    
}
// @lc code=end

