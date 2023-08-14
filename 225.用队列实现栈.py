#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:
    # 队列：先进先出
    # 栈：后进先出
    def __init__(self):
        self.list1 = []
        self.list2 = []

    def push(self, x: int) -> None:
        self.list1.append(x)
        while self.list2:
            self.list1.append(self.list2.pop(0))
        self.list1, self.list2 = self.list2, self.list1

    def pop(self) -> int:
        return self.list2.pop(0)

    def top(self) -> int:
        return self.list2[0]


    def empty(self) -> bool:
        return not self.list1 and not self.list2



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

