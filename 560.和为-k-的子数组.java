/*
 * @lc app=leetcode.cn id=560 lang=java
 *
 * [560] 和为 K 的子数组
 */

// @lc code=start
import java.util.HashMap;
class Solution {
    public int subarraySum(int[] nums, int k) {
        //前缀和
        int res = 0;
        int n = nums.length;
        int[] prefix = new int[n+1]; //默认为0
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0,1);
        for(int i=1;i<n+1;i++){
            prefix[i] = prefix[i-1] + nums[i-1];
            int target = prefix[i] - k;
            res += map.getOrDefault(target, 0);
            map.put(prefix[i], map.getOrDefault(prefix[i], 0)+1);
        }
        return res;
    }
}
// @lc code=end

