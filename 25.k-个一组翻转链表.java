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
            if(b==null)return head;
            b = b.next;
        }
        ListNode newNode = reverseLink(a, b);
        a.next = reverseKGroup(b, k);
        return newNode;
    }

    public ListNode reverseLink(ListNode head, ListNode tail){
        if(head.next==tail)return head;
        ListNode root = reverseLink(head.next, tail);
        head.next.next = head;
        head.next = null;
        return root;
    }
}
// @lc code=end

