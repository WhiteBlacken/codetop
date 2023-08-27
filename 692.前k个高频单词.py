#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#

# @lc code=start
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = {}
        for word in words:
            dict[word] = dict.get(word, 0) + 1
        heap = []
        for key in dict:
            customElement = CustomElement(dict[key], key)
            heapq.heappush(heap, (customElement))
        res = []
        while k > 0:
            element = heapq.heappop(heap)
            res.append(element.val2)
            k -= 1
        return res


class CustomElement:
    def __init__(self, val1, val2) -> None:
        self.val1 = val1
        self.val2 = val2
    
    def __lt__(self, other):
        if self.val1 == other.val1:
            return self.val2 < other.val2
        return self.val1 > other.val1
# @lc code=end

