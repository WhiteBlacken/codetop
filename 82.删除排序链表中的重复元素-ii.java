/*
 * @lc app=leetcode.cn id=82 lang=java
 *
 * [82] 删除排序链表中的重复元素 II
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
        //和删除重复元素1的区别是，这个只要出现重复，就一个也不保留
        if(head==null||head.next==null)return head;
        //反正为了简化操作，都加个虚拟头得了
        ListNode dummy = new ListNode(-101), cur = dummy;
        //如果一个元素，和他前后均不同，则可以加入dummy
        ListNode pre = dummy;
        while(head!=null){
            if(head.val!=pre.val&&(head.next==null||head.val!=head.next.val)){
                cur.next = head;
                cur = cur.next;
                pre = head;
                head = head.next;
                cur.next = null;
            }else{
                pre = head;
                head = head.next;
            }
            
        }
        return dummy.next;

    }
}
// @lc code=end

