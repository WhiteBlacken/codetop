#
# @lc app=leetcode.cn id=381 lang=python3
#
# [381] O(1) 时间插入、删除和获取随机元素 - 允许重复
#

# @lc code=start
import random
class RandomizedCollection:
    # 与基础版的区别是：允许重复
    # 那简单的dict就不好使了
    # get random的要求，和“按权重随机返回”一致，考虑使用前缀和+二分，但是时间复杂度非O(1)
    # 直接 dict[a] = []完事了,其他和基础版一样
    # 怎么保证插进list的是最大值？插几次就乱了，查找list也是O(n),用set

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            self.dict[val].add(len(self.list))
        else:
            self.dict[val] = set()
            self.dict[val].add(len(self.list))
        self.list.append(val)
        return len(self.dict[val]) == 1

    def remove(self, val: int) -> bool:
        if val in self.dict:
            index = self.dict[val].pop() # 拿到其中一个下标,并移除该元素
            if len(self.dict[val]) == 0: # 如果元素都移除完了，则删去key
                self.dict.pop(val) 
            if index != len(self.list) - 1: # 如果已经为最后一位了，不需要交换
                self.list[-1], self.list[index] = self.list[index], self.list[-1] # 待删除交换到list末尾
                self.dict[self.list[index]].remove(len(self.list)-1) # 从中删除数组最后的index,这一步是使用set的原因
                self.dict[self.list[index]].add(index) # 增加新的index
            self.list.pop() # 删除数组最后一个元素
            return True
        return False


    def getRandom(self) -> int:
        index = random.randint(0, len(self.list)-1)
        return self.list[index]



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

