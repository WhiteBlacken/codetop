/*
 * @lc app=leetcode.cn id=5 lang=java
 *
 * [5] 最长回文子串
 */

// @lc code=start
class Solution {
    public String longestPalindrome(String s) {
        //针对n个字母，每个做一次回文子串判断，取最大值
        String res = s.substring(0, 1);
        //奇数中心
        for(int i=1;i<s.length()-1;i++){ //第一个和最后一个不用判断
            int left= i-1,right = i + 1;
            while(left>=0&&right<s.length()&&s.charAt(left)==s.charAt(right)){
                left--;
                right++;
            }
            if(right-left-1>res.length()){ //因为跳出范围了
                res = s.substring(left+1, right);
            }
        }
        //偶数中心
        for(int i=0;i<s.length()-1;i++){
            if(s.charAt(i)!=s.charAt(i+1))continue;
            int left = i-1, right= i+2;
            while(left>=0&&right<s.length()&&s.charAt(left)==s.charAt(right)){
                left--;
                right++;
            }
            if(right-left-1>res.length()){ //因为跳出范围了
                res = s.substring(left+1, right);
            }
        }
        return res;

    }
}
// @lc code=end

