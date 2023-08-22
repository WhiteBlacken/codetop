/*
 * @lc app=leetcode.cn id=90 lang=java
 *
 * [90] 子集 II
 */

// @lc code=start

import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

class Solution {
    List<List<Integer>> res = new ArrayList<>();
    //集合和序列有区别
    //4,4,2,4,4 考虑 442和244
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        backtrack(0, nums, new ArrayList<>());
        return res;
    }

    public void backtrack(int start, int[] nums, List<Integer> tmp){
        res.add(new ArrayList<>(tmp));
        for(int i=start;i<nums.length;i++){
            if(i>start&&nums[i]==nums[i-1])continue;
            tmp.add(nums[i]);
            backtrack(i+1, nums, tmp);
            tmp.remove(tmp.size()-1);
        }
    }
}
// @lc code=end

