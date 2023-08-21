/*
 * @lc app=leetcode.cn id=409 lang=java
 *
 * [409] 最长回文串
 */

// @lc code=start
import java.util.HashMap;
class Solution {
    public int longestPalindrome(String s) {
        int res = 0;
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i=0;i<s.length();i++){
            Character key = s.charAt(i);
            if(map.containsKey(key)){
                map.put(key, map.get(key)+1);
            }
            else{
                map.put(key, 1);
            }
        }
        int addOne = 0;
        for(Character ch: map.keySet()){
            if(map.get(ch)%2==1)addOne=1;
            res += map.get(ch)/2*2;
        }
        return res+addOne;

    }
}
// @lc code=end

