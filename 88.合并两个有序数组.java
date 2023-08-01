/*
 * @lc app=leetcode.cn id=88 lang=java
 *
 * [88] 合并两个有序数组
 */

// @lc code=start
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int cur = m + n - 1;
        m = m - 1;
        n = n - 1;
        while (m >= 0 && n >= 0) {
            if (nums1[m] > nums2[n]) {
                nums1[cur] = nums1[m];
                m -= 1;
            } else {
                nums1[cur] = nums2[n];
                n -= 1;
            }
            cur -= 1;
        }
   
        while (m >= 0) {
            nums1[cur] = nums1[m];
            m -= 1;
            cur -= 1;
        }
        while (n >= 0) {
            nums1[cur] = nums2[n];
            n -= 1;
            cur -= 1;
        }

    }
}
// @lc code=end
