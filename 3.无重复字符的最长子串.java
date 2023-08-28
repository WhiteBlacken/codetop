/*
 * @lc app=leetcode.cn id=3 lang=java
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start

import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length()<=1)return s.length();
        HashMap<Character, Integer> map = new HashMap<>();
        int win = 0;
        int left = 0; 
        int n = s.length();
        for(int right=0;right<n;right++){
            char ch = s.charAt(right);
            if(map.containsKey(ch)&&map.get(ch)>=left){ //验证未被排除在窗口之外
                left = map.get(ch)+1;
            }else{
                win = Math.max(win, right-left+1);
            }
            map.put(ch, right); //一次只会重复一个，旧的已经被排除了
        }
        return win;
    }
}
// @lc code=end

