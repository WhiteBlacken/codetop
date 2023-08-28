/*
 * @lc app=leetcode.cn id=49 lang=java
 *
 * [49] 字母异位词分组
 */

// @lc code=start

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        //异位词就是不看顺序，只看每种字母的数量？
        //先来个笨比做法
        HashMap<String, List<Integer>> map = new HashMap<>();
        for(int j=0;j<strs.length;j++){
            String str = strs[j];
            int[] counts = new int[26]; //默认赋值0
            for(int i=0;i<str.length();i++){
                int idx = str.charAt(i) - 'a';
                counts[idx] += 1;
            }
            String id = list2String(counts);
            if(map.containsKey(id)){
                List<Integer> nums = map.get(id);
                nums.add(j);   
                map.put(id, nums);
            }else{
                List<Integer> nums = new ArrayList<>();
                nums.add(j);
                map.put(id, nums);
            }
        }
        List<List<String>> res = new ArrayList<>();
        for(String s: map.keySet()){
            List<String> tmp = new ArrayList<>();
            for(int idx: map.get(s)){
                tmp.add(strs[idx]);
            }
            res.add(tmp);
        }
        return res;
    }

    String list2String(int[] counts){
        String res = "";
        for(int count: counts){
            res += String.valueOf(count) + "-";
        }
        return res;
    }
}
// @lc code=end

