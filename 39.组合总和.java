/*
 * @lc app=leetcode.cn id=39 lang=java
 *
 * [39] 组合总和
 */

// @lc code=start

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        //其实就是求不同的组合
        backtrack(0, new ArrayList<>(), target, candidates);
        return res;
    }
    
    void backtrack(int start, List<Integer> tmp, int target, int[] candidates){
        int sum = tmp.stream().mapToInt(Integer::intValue).sum();
        if(sum==target){
            res.add(new ArrayList<>(tmp));
            return;
        }
        if(sum>target)return;

        for(int i=start;i<candidates.length;i++){
            tmp.add(candidates[i]);
            backtrack(i, tmp, target, candidates); //起始位置决定是否能重复使用数字
            tmp.remove(tmp.size()-1);
        }
    }
}
// @lc code=end

