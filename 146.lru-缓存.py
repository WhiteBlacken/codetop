#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.doubleList = DoubleList()
        self.map = {} # 记录位置

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.doubleList.remove(node)
            self.doubleList.addList(node)
            return node.value
        return -1


    def put(self, key: int, value: int) -> None: 
        node = Node(key, value)
        if key in self.map:
            # 删除原有
            self.doubleList.remove(self.map[key])
        self.doubleList.addList(node)
        self.map[key] = node # update or add
        if self.doubleList.size > self.capacity: # 需要删除结点
            old_node = self.doubleList.removeFirst()
            del self.map[old_node.key]

class Node:
    def __init__(self, k: int, v: int) -> None:
        self.key = k
        self.value = v
        self.next = None
        self.prev = None

class DoubleList:
    def __init__(self) -> None:
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def addList(self, x: Node):
        last = self.tail.prev
        last.next = x
        x.prev = last
        x.next = self.tail
        self.tail.prev = x
        self.size += 1

    def remove(self, x: Node):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1
        

    def removeFirst(self) -> Node:
        first = self.head.next
        self.remove(first)
        return first

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

