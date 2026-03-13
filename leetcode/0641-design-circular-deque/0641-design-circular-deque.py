class ListNode:
    def __init__(self, value=0, next = None, prev = None):
        self.val = value
        self.next = next
        self.prev = next
class MyCircularDeque:

    def __init__(self, k: int):
        self.maxSize = k
        self.listSize = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.listSize == self.maxSize:
            return False

        curr = ListNode(value)
        
        if not self.head:
            self.head = self.tail = curr
            self.head.next = self.head
        else:
            curr.next = self.head
            self.head.prev = curr
            self.tail.next = curr
            curr.prev = self.tail
            self.head = curr
        self.listSize += 1

        return True
        
    
        
        

    def insertLast(self, value: int) -> bool:
        
        if self.listSize == self.maxSize:
            return False
        
        curr = ListNode(value)
        if not self.head:
            self.head = self.tail = curr
            self.head.next = self.head
            self.tail.prev = self.head
        else:
            self.tail.next = curr
            curr.prev = self.tail
            curr.next = self.head
            self.tail = curr
            self.head.prev = self.tail
        self.listSize += 1
        return True

    def deleteFront(self) -> bool:
        if self.listSize == 0:
            return False
        if self.listSize == 1:
            self.head = self.tail = None
        else:  
            curr = self.head
            self.head = self.head.next
            curr.next = curr.prev = None
            self.head.prev = self.tail
            self.tail.next = self.head
        self.listSize -= 1
        return True

        
    def deleteLast(self) -> bool:
        if self.listSize == 0:
            return False
        
        if self.listSize == 1:
            self.head = self.tail = None
        else:
            curr = self.tail
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            curr.prev = curr.next = None

        self.listSize -= 1
        return True
        
        
    def getFront(self) -> int:
        if self.listSize == 0:
            return -1
        return self.head.val

    def getRear(self) -> int:
        if self.listSize == 0:
            return -1
        return self.tail.val
    def isEmpty(self) -> bool:
        return self.listSize == 0

    def isFull(self) -> bool:
        return self.listSize == self.maxSize


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()