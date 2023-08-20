/*
 * @lc app=leetcode.cn id=125 lang=java
 *
 * [125] 验证回文串
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(String s) {
        int left=0,right=s.length()-1;
        while(left<right){
            while(left<right&&!Character.isLetterOrDigit(s.charAt(left)))left++;
            while(left<right&&!Character.isLetterOrDigit(s.charAt(right)))right--;
            char l_ch = s.charAt(left);
            char r_ch = s.charAt(right);
            if(Character.toLowerCase(l_ch)!=Character.toLowerCase(r_ch)){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
// @lc code=end

