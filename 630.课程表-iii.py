#
# @lc app=leetcode.cn id=630 lang=python3
#
# [630] 课程表 III
#

# @lc code=start
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # 贪心
        courses.sort(key=lambda x:x[1])
        max_heap = []
        ddl = 0
        for course in courses:
            if ddl + course[0] <= course[1]:
                ddl += course[0]
                heapq.heappush(max_heap, -course[0])
            elif max_heap and -max_heap[0] > course[0]:
                ddl += course[0] + heapq.heappop(max_heap) # 因为是负数，实际是减
                heapq.heappush(max_heap, -course[0])
        return len(max_heap)
        
# @lc code=end

