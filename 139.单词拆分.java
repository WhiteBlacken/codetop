/*
 * @lc app=leetcode.cn id=139 lang=java
 *
 * [139] 单词拆分
 */

// @lc code=start

import java.util.*;
class Solution {
    private Map<String,Boolean> memx = new HashMap<>();
    public boolean wordBreak(String s, List<String> wordDict) {
        return backtrack(s, new HashSet<>(wordDict));

    }

    boolean backtrack(String s, Set<String> wordDict){
        if(memx.containsKey(s))return memx.get(s);
        if(s.length()==0)return true;
        boolean res = false;
        for(int i=0;i<s.length();i++){
            if(wordDict.contains(s.substring(0, i+1))){
                res = res || backtrack(s.substring(i+1, s.length()), wordDict);
            }
        }
        memx.put(s,res);
        return res;

    }
}
// @lc code=end

