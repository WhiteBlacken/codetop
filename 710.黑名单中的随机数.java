/*
 * @lc app=leetcode.cn id=710 lang=java
 *
 * [710] 黑名单中的随机数
 */

// @lc code=start
import java.util.Random;
import java.util.HashMap;
import java.util.Map;

class Solution {
    //紧凑的数组才是好数组
    private int sz; //实际有效的范围
    private int[] blacklist;
    private Map<Integer, Integer> map = new HashMap<>();

    public Solution(int n, int[] blacklist) {
        this.sz = n - blacklist.length;
        this.blacklist = blacklist;
        for(int a:blacklist){
            map.put(a, 666); //做标记
        }
        int right = this.sz;
        for(Map.Entry<Integer, Integer> entry:map.entrySet()){
                if(entry.getKey()<this.sz){ //需要交换
                    while(map.containsKey(right)&&map.get(right)==666)right++;
                    map.put(entry.getKey(), right);
                    right++;
                }
        }
        
    }
    
    public int pick() {
        Random random = new Random();
        int num = random.nextInt(sz);
        if(map.containsKey(num)){
            return map.get(num);
        }
        return num;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(n, blacklist);
 * int param_1 = obj.pick();
 */
// @lc code=end

