class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]

    def hash(self, num):
        return num % 1000  

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        curr = self.map[index]

        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                break
            curr = curr.next  
        else:
            curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self.hash(key)
        curr = self.map[index].next

        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        curr = self.map[index]

        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                break
            curr = curr.next



        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna