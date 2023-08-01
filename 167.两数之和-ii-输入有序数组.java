/*
 * @lc app=leetcode.cn id=167 lang=java
 *
 * [167] 两数之和 II - 输入有序数组
 */

// @lc code=start
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        //也可以使用dict，不过需要额外的空间，本题已经有序，直接双指针
        int left = 0, right = numbers.length - 1;
        while(left<right){
            int tmp = numbers[left]+numbers[right];
            if(tmp==target)return new int[]{left+1,right+1};
            if(tmp>target){
                right--;
            }else{
                left++;
            }
        }
        return new int[]{};

    }
}
// @lc code=end

