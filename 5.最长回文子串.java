/*
 * @lc app=leetcode.cn id=5 lang=java
 *
 * [5] 最长回文子串
 */

// @lc code=start
class Solution {
    public String longestPalindrome(String s) {
        String s1 = longestPalindromeOdd(s);
        String s2 = longestPalindromeDouble(s);
        return s1.length()>s2.length() ? s1:s2;
    }

    String longestPalindromeOdd(String s){
        String max_res = "";
        for(int i=0;i<s.length();i++){
            int l=i-1,r=i+1;
            while(l>=0&&r<s.length()&&s.charAt(l)==s.charAt(r)){
                l--;
                r++;
            }
            if(r-l-1>max_res.length()){//两边分别越界1
                max_res = s.substring(l+1, r);
            } 
        }
        return max_res;
    }

    String longestPalindromeDouble(String s){
        String max_res = "";
        for(int i=0;i<s.length()-1;i++){
            if(s.charAt(i)!=s.charAt(i+1))continue;
            int l=i-1,r=i+2;
            while(l>=0&&r<s.length()&&s.charAt(l)==s.charAt(r)){
                l--;
                r++;
            }
            if(r-l-1>max_res.length()){
                max_res = s.substring(l+1, r);
            }
        }
        return max_res;
    }
}
// @lc code=end

