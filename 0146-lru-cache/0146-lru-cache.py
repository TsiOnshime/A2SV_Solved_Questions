class ListNode:
    def __init__(self,key, value):
        self.key, self.value = key, value
        self.next, self.prev = None, None
class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        self.cache = {}
        self.k = 0
        self.capacity = capacity
        
    def remove(self, node):

        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        self.k -= 1

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, node.prev = node, prev
        nxt.prev, node.next = node, nxt
        self.k += 1
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = ListNode(key, value)
        self.cache[key] = node
        self.insert(node)

        if self.k > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# key: value => hashmap

# to maintain the lru and mru 
# I would use linked list

# key: node => key, val and pre, next
# left : lru
# right: mru
# 4: 5, 6:5, 6:6, 7:6
# <= left =><= 3,3 =><= 6,5 =><= right => 
            #          prev=><=node=><=next