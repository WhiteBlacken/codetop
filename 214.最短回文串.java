/*
 * @lc app=leetcode.cn id=214 lang=java
 *
 * [214] 最短回文串
 */

// @lc code=start
class Solution {
    public String shortestPalindrome(String s) {
        //string+string的逆转，中间要除去本身就回文的前缀
        String s_rev = new StringBuilder(s).reverse().toString();
        String s_new = s + "#" + s_rev;
        int[] prefix = computePreifx(s_new);
        int len = prefix[s_new.length()-1];
        return s_rev.substring(0, s.length()-len) + s;
    }

    public int[] computePreifx(String s){
        int[] prefix = new int[s.length()];
        int j = 0;
        for(int i=1;i<s.length();i++){
            while(j>0&&s.charAt(i)!=s.charAt(j))j=prefix[j-1];
            if(s.charAt(i)==s.charAt(j))j++;
            prefix[i] = j;
        }
        return prefix;
    }
}
// @lc code=end

