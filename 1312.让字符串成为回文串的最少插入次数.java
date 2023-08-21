/*
 * @lc app=leetcode.cn id=1312 lang=java
 *
 * [1312] 让字符串成为回文串的最少插入次数
 */

// @lc code=start
import java.util.HashMap;
class Solution {
    private HashMap<String,Integer> memx = new HashMap<>();

    public int minInsertions(String s) {
        return minString(s);

    }
    public int minString(String s){
        if(s.length()<=1)return 0;
        if(memx.containsKey(s))return memx.get(s);
        //最小-动态规划方向考虑
        //选择，面临不一致时，插左边，插右边，不用真的插，就是不动指针
        int left = 0, right = s.length() - 1;
        int length = 0;
        while(left<right){
            if(s.charAt(left)!=s.charAt(right)){
                length++;
                length += Math.min(
                    minString(s.substring(left, right)), 
                    minString(s.substring(left+1, right+1)));
                memx.put(s, length);
                return length;
            }
            left++;
            right--;
        }
        memx.put(s, length);
        return length;
    }
}
// @lc code=end

