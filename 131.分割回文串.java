/*
 * @lc app=leetcode.cn id=131 lang=java
 *
 * [131] 分割回文串
 */

// @lc code=start

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<List<String>> res = new ArrayList<>();
    public List<List<String>> partition(String s) {
        //这就是个回溯，worddict那题一样
        backtrack(s, new ArrayList<>());
        return res;
    }

    public void backtrack(String s, List<String> tmp){
        if(s.isEmpty()){
            res.add(new ArrayList<>(tmp));
            return;
        }
        for(int i=0;i<s.length();i++){
            if(!isPa(s.substring(0, i+1)))continue;
            tmp.add(s.substring(0, i+1));
            backtrack(s.substring(i+1, s.length()), tmp);
            tmp.remove(tmp.size()-1);
        }
    }


    public boolean isPa(String s){
        int left=0,right=s.length()-1;
        while(left<right){
            if(s.charAt(left)!=s.charAt(right))return false;
            left++;
            right--;
        }
        return true;
    }
}
// @lc code=end

