/*
 * @lc app=leetcode.cn id=442 lang=java
 *
 * [442] 数组中重复的数据
 */

// @lc code=start

import java.util.LinkedList;
import java.util.List;
class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        //数字范围是[1,n],下标范围是[0,n-1]
        List<Integer> res = new LinkedList<>();
        for(int num: nums){
            int idx = Math.abs(num)-1;
            int val = nums[idx];
            if(val<0){
                res.add(Math.abs(num));
            }
            nums[idx] = -nums[idx];
        }
        return res;
    }
}
// @lc code=end

