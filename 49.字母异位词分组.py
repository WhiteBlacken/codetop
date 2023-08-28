#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = {}
        for i, string in enumerate(strs):
            nums = [0]*26
            for item in string:
                idx = ord(item) - ord('a')
                nums[idx] += 1
            id = self.list2String(nums)
            if id in dict:
                dict[id].append(i)
            else:
                dict[id] = [i]
        res = []
        for key in dict:
            tmp = []
            for item in dict[key]:
                tmp.append(strs[item])
            res.append(tmp)
        return res
    
    def list2String(self, nums):
        string = ""
        for num in nums:
            string += str(num) + "-"
        return string
# @lc code=end

