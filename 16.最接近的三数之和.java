/*
 * @lc app=leetcode.cn id=16 lang=java
 *
 * [16] 最接近的三数之和
 */

// @lc code=start
import java.util.Arrays;
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        //爆搜可以，但是时间复杂度高
        //和3数之和肯定有关系
        int res = nums[0] + nums[1] + nums[2];
        Arrays.sort(nums);
        for(int i=0;i<nums.length-2;i++){
            int start = i+1;
            int end = nums.length - 1;
            while(start<end){
                int tmp = nums[i] + nums[start] + nums[end];
                if(tmp==target)return tmp; 
                if(Math.abs(tmp-target)<Math.abs(res-target)){
                    res = tmp;
                }
                if(tmp>target){
                    end--;
                }else{
                    start++;
                }
            }

        }
        return res;

    }
}
// @lc code=end

