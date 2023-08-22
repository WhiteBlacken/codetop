/*
 * @lc app=leetcode.cn id=491 lang=java
 *
 * [491] 递增子序列
 */

// @lc code=start
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.HashSet;
class Solution {
    List<List<Integer>> res = new LinkedList<>();
    List<Integer> path = new ArrayList<>();

    public List<List<Integer>> findSubsequences(int[] nums) {
        backtrack(0, nums, new LinkedList<>());
        return res;
    }
    //找出所有的子集
    //如何处理重复数字，此处和子集II不一样，不能先排序
    public void backtrack(int start, int[] nums, List<Integer> tmp){
        if(isValid(tmp))res.add(new LinkedList<>(tmp));
        HashSet<Integer> uset = new HashSet<>();
        for(int i=start;i<nums.length;i++){
            if(uset.contains(nums[i]))continue;
            uset.add(nums[i]);
            tmp.add(nums[i]);
            backtrack(i+1, nums, tmp);
            tmp.remove(tmp.size()-1);
        }
    }
    public boolean isValid(List<Integer> tmp){
        if(tmp.size()<=1)return false;
        for(int i=1;i<tmp.size();i++){
            if(tmp.get(i)<tmp.get(i-1))return false;
        }
        return true;
    }
}
// @lc code=end

