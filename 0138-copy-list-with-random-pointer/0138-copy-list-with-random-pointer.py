"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        curr = head
        while curr:
            temp = Node(curr.val)
            nxt = curr.next
            curr.next = temp
            temp.next = nxt
            curr = curr.next.next
        
        curr = head
        while curr:
            temp = curr.next
            temp.random = curr.random.next if curr.random else None

            curr = curr.next.next
        curr = head
        dummy = Node(0)
        res = dummy
        while curr:
            temp = curr.next.next if curr.next else None
            res.next = curr.next
            curr.next = temp
            curr = temp
            res = res.next
        return dummy.next
        

            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna