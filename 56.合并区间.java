/*
 * @lc app=leetcode.cn id=56 lang=java
 *
 * [56] 合并区间
 */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
// @lc code=start
class Solution {
    public int[][] merge(int[][] intervals) {
        //只和左端点有关
        Arrays.sort(intervals, (a,b) -> a[0]-b[0]);
        List<int[]> res = new ArrayList<>();
        int start = 0,end = 0,i = 0;
        while(i<intervals.length){
            start = intervals[i][0];
            end = intervals[i][1];

            while(i<intervals.length&&end>=intervals[i][0]){ //重复计算了自身，不过无所谓
                end = Math.max(end,intervals[i][1]);
                i += 1;
            }
            res.add(new int[]{start, end});

        }
        return res.toArray(new int[res.size()][]);
        
        
    }
}
// @lc code=end

