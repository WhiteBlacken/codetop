/*
 * @lc app=leetcode.cn id=1 lang=java
 *
 * [1] 两数之和
 */
import java.util.Map;
import java.util.HashMap;
// @lc code=start
class Solution {
    public int[] twoSum(int[] nums, int target) {
        //返回值为下标，而排序会破坏下标
        //使用dict
        Map<Integer,Integer> hashMap = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(hashMap.containsKey(target-nums[i])){
                return new int[]{i, hashMap.get(target-nums[i])};
            }
            hashMap.put(nums[i], i);
        }
        return new int[]{};
    }
}
// @lc code=end

