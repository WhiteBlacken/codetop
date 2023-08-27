/*
 * @lc app=leetcode.cn id=91 lang=java
 *
 * [91] 解码方法
 */

// @lc code=start
class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        int[] dp = new int[n];
        if(valid(s.substring(0, 1)))dp[0]=1;
        if(s.length()<=1)return dp[0];
        for(int i=1;i<n;i++){
            if(valid(s.substring(i, i+1)))dp[i] += dp[i-1]; //往前推1个的
            if(i==1){
                if(valid(s.substring(i-1, i+1)))dp[i] += 1; //往前推2个的
            }else{
                if(valid(s.substring(i-1, i+1)))dp[i] += dp[i-2];
            }
        }
        return dp[n-1];
    }
    public boolean valid(String s){
        int num = Integer.parseInt(s);
        if(s.length()==1){
            if(num>0&&num<10)return true;
        }else if(s.length()==2){
            if(num>=10&&num<=26)return true;
        }
        return false;
    }
}
// @lc code=end

