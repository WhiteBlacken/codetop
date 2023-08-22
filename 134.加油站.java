/*
 * @lc app=leetcode.cn id=134 lang=java
 *
 * [134] 加油站
 */

// @lc code=start
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        int totalGas,totatCost,tank,start;
        totalGas=totatCost=tank=start=0;
        for(int i=0;i<n;i++){
            totalGas += gas[i];
            totatCost += cost[i];
            tank += gas[i] - cost[i];
            if(tank<0){
                tank=0;
                start=i+1;
            }
        }
        if(totalGas<totatCost)return -1;
        return start;
    }
}
// @lc code=end

