/*
 * @lc app=leetcode.cn id=18 lang=java
 *
 * [18] 四数之和
 */

// @lc code=start
import java.util.Arrays;

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        // 三数之和上套娃
        // 该题要注意类型转换
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int i = 0;
        while (i < nums.length) {
            List<List<Integer>> items = threeSum(Arrays.copyOfRange(nums, i + 1, nums.length), target - nums[i]);
            for (List<Integer> item : items) {
                List<Integer> four = new ArrayList<>();
                four.add(nums[i]);
                four.addAll(item);
                res.add(four);
            }
            while (i + 1 < nums.length && nums[i] == nums[i + 1])
                i++;
            i++;
        }
        return res;

    }

    public List<List<Integer>> threeSum(int[] nums, long target) {
        // 需要的不是下标，可以排序
        List<List<Integer>> res = new ArrayList<>();
        int i = 0;
        while (i < nums.length) {
            List<List<Integer>> items = twoSum(Arrays.copyOfRange(nums, i + 1, nums.length), target - (long) nums[i]);
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

    public List<List<Integer>> twoSum(int[] nums, long target) {
        int left = 0, right = nums.length - 1;
        List<List<Integer>> res = new ArrayList<>();
        while (left < right) {
            long tmp = (long) nums[left] + (long) nums[right];
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
