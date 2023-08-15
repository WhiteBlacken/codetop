/*
 * @lc app=leetcode.cn id=630 lang=java
 *
 * [630] 课程表 III
 */

// @lc code=start
import java.util.Arrays;
import java.util.PriorityQueue;


class Solution {
    public int scheduleCourse(int[][] courses) {
        //贪心，修ddl在前的，但是要是超时了，就删去时间最长的
        Arrays.sort(courses, ((a,b)->Integer.compare(a[1], b[1])));
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a,b)->Integer.compare(b, a));
        int ddl = 0;
        for(int[] course: courses){
            if(ddl+course[0]<=course[1]){
                ddl += course[0];
                maxHeap.offer(course[0]);
            }else if(!maxHeap.isEmpty() && maxHeap.peek() > course[0]){
                ddl = ddl - maxHeap.poll() + course[0];
                maxHeap.offer(course[0]);
            }
        }
        return maxHeap.size();
    }
}
// @lc code=end

