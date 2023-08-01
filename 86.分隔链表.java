/*
 * @lc app=leetcode.cn id=86 lang=java
 *
 * [86] 分隔链表
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
    public ListNode partition(ListNode head, int x) {
        //感觉像是快速排序
        //暴力解法，把小于的都挑出来：只有常数级空间开销，时间复杂度O(n)
        ListNode dummy1 = new ListNode(-1), dummy2 = new ListNode(-1);
        ListNode cur1 = dummy1, cur2 = dummy2;
        while(head!=null){
            if(head.val < x){
                cur1.next = head;
                head = head.next;
                cur1 = cur1.next;
                cur1.next = null;
            }else{
                cur2.next = head;
                head = head.next;
                cur2 = cur2.next;
                cur2.next = null;
            }
        }
        cur1.next = dummy2.next;
        return dummy1.next;
    }
}
// @lc code=end

