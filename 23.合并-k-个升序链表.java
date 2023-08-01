/*
 * @lc app=leetcode.cn id=23 lang=java
 *
 * [23] 合并 K 个升序链表
 */

// @lc code=start

import java.util.Arrays;
import java.util.PriorityQueue;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> minHeap = new PriorityQueue<>((a,b)->a.val-b.val);
        for(ListNode list:lists){
            if(list!=null)minHeap.offer(list);
        }
        ListNode dummy = new ListNode(-1);
        ListNode cur = dummy;
        while(!minHeap.isEmpty()){ //listnode为null，则不加入minheap.
            ListNode node = minHeap.poll();
            cur.next = node;
            cur = cur.next;
            if(cur.next!=null){
                minHeap.offer(cur.next);
            }
        }
        return dummy.next;
    }
}
// @lc code=end
