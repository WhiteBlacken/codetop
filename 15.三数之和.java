/*
 * @lc app=leetcode.cn id=15 lang=java
 *
 * [15] 三数之和
 */

// @lc code=start

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // 需要的不是下标，可以排序
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int i = 0;
        while (i < nums.length) {
            List<List<Integer>> items = twoSum(Arrays.copyOfRange(nums, i + 1, nums.length), -nums[i]);
            for (List<Integer> item : items) {
                List<Integer> triple = new ArrayList<>();
                triple.add(nums[i]);
                triple.addAll(item);
                res.add(triple);
            }
            while (i + 1 < nums.length && nums[i] == nums[i + 1])
                i++;
            i++;
        }
        return res;

    }

    public List<List<Integer>> twoSum(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        List<List<Integer>> res = new ArrayList<>();
        while (left < right) {
            int tmp = nums[left] + nums[right];
            if (tmp == target) {
                res.add(Arrays.asList(nums[left], nums[right]));
                right--;
                left++;
                while (left < right && nums[right] == nums[right + 1]) {
                    right--;
                }
                while (left < right && nums[left] == nums[left - 1]) {
                    left++;
                }

            } else if (tmp > target) {
                right--;
            } else {
                left++;
            }
        }
        return res;

    }
}
// @lc code=end
