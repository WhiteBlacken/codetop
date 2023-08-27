/*
 * @lc app=leetcode.cn id=233 lang=java
 *
 * [233] 数字 1 的个数
 */

// @lc code=start
class Solution {
    public int countDigitOne(int n) {
        int res = 0;
        for(int i=1;i<=n;i++)res+=getOneNum(i);
        return res;
    }
    int getOneNum(int n){
        int res = 0;
        while(n>0){
            if(n%10==1)res+=1;
            n = n/10;
        }
        return res;
    }
}
// @lc code=end

