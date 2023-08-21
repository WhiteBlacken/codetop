/*
 * @lc app=leetcode.cn id=516 lang=java
 *
 * [516] 最长回文子序列
 */

// @lc code=start
import java.util.HashMap;
class Solution {
    private HashMap<String, Integer> memx = new HashMap<>();
    public int longestPalindromeSubseq(String s) {
        return longestString(s);
    }
    public int longestString(String s){
        if(memx.containsKey(s))return memx.get(s);
        // base case的处理
        if(s.length()<=0)return 0;
        if(s.length()==1)return 1;

        int length = 0;
        int left=0,right=s.length()-1;
        while(left<=right){
            int add = 2;
            if(left==right)add=1;
            if(s.charAt(left)==s.charAt(right))length+=add;
            else{
                length += Math.max(
                    longestPalindromeSubseq(s.substring(left+1, right+1)),
                    longestPalindromeSubseq(s.substring(left, right)));
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

