/*
 * @lc app=leetcode.cn id=46 lang=java
 *
 * [46] 全排列
 */

// @lc code=start

import java.util.ArrayList;
import java.util.List;

class Solution {
    
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        boolean[] visited = new boolean[nums.length];
        order(nums, new ArrayList<>(), visited, res);
        return res;
    }
    public void order(int[] nums, List<Integer> tmp, boolean[] visited, List<List<Integer>> res){
        if(tmp.size()==nums.length){
            res.add(new ArrayList<>(tmp));
            return;
        }
        for(int i=0;i<nums.length;i++){
            if(visited[i])continue;
            visited[i] = true;
            tmp.add(nums[i]);
            order(nums, tmp, visited, res);
            tmp.remove(tmp.size()-1);
            visited[i] = false;
        }
    }

}
// @lc code=end

