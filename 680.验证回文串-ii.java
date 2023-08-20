/*
 * @lc app=leetcode.cn id=680 lang=java
 *
 * [680] 验证回文串 II
 */

// @lc code=start

class Solution {
    public boolean validPalindrome(String s) {
        return validString(s, true);
    }
    public boolean validString(String s, boolean canDel){
        int left=0,right=s.length()-1;
        while(left<right){
            char l_ch = s.charAt(left);
            char r_ch = s.charAt(right);
            if(l_ch!=r_ch){
                if(!canDel)return false;
                return validString(s.substring(left+1, right+1), false) || validString(s.substring(left, right), false);
            }
            left++;
            right--;
        }
        return true;
    }
}
// @lc code=end

