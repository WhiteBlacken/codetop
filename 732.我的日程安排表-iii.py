#
# @lc app=leetcode.cn id=732 lang=python3
#
# [732] 我的日程安排表 III
#

# @lc code=start
class MyCalendarThree:
    # 很明显的区间更新问题
    # 如果使用差分，每次返回最大预定，都需要更新一次数组，差分的优势就没了（多次更新，一次查询）
    # 而且这个数组怎么开？10**9 -> 所以线段树，动态开点吧
    def __init__(self):
        


    def book(self, startTime: int, endTime: int) -> int:



# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
# @lc code=end

