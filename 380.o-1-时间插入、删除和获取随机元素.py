#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start
import random
class RandomizedSet:
    # O(1)插入和删除，是字典的性质
    # 随机返回，下标访问，是数组的性质
    # 数组删除操作不是O(1)
    
    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            index = self.dict[val]
            # 交换到最后再删除
            self.list[-1], self.list[index] = self.list[index], self.list[-1]
            # 更新dict
            self.dict[self.list[index]] = index
            self.list.pop() # 这种是O(1)
            self.dict.pop(val)
            return True
        return False


    def getRandom(self) -> int:
        index = random.randint(0, len(self.list)-1)
        return self.list[index]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

