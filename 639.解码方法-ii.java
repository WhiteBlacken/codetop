/*
 * @lc app=leetcode.cn id=639 lang=java
 *
 * [639] 解码方法 II
 */

// @lc code=start

class Solution {
    private static final int mod = 1_000_000_007;
    private long[] dp = new long[100003];
    public int numDecodings(String s) {
        //是乘法不是加法
        dp[0] = 1;
        dp[1] = (s.charAt(0) == '*' ? 9:1);
        if(s.charAt(0)=='0')dp[0] = dp[1] = 0;
        for(int i=1;i<s.length();i++){
            if(s.charAt(i)!='*'){
                if(s.charAt(i) != '0') dp[i+1] = dp[i];
                if(s.charAt(i-1)=='1') dp[i+1] += dp[i-1];
                else if(s.charAt(i-1)=='2'&&s.charAt(i)<'7') dp[i+1] += dp[i-1];
                else if(s.charAt(i-1) == '*'){
                    if(s.charAt(i)<'7')dp[i+1] += (dp[i-1]*2);
                    else dp[i+1] += dp[i-1];
                }

            }else{
                dp[i+1] = dp[i]*9;
                if(s.charAt(i-1)=='1'){
                    dp[i+1] += dp[i-1]*9;
                }else if(s.charAt(i-1)=='2'){
                    dp[i+1] += dp[i-1]*6;
                }else if(s.charAt(i-1)=='*'){
                    dp[i+1] += dp[i-1]*15;
                }
            }
            dp[i+1] %= mod;
        }

        return (int)dp[s.length()];
    }
}
// @lc code=end

