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
        if not head:
            return None
        curr = head
        while curr:
            newNode = Node(curr.val)
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next

        # 7 => 7 => 13 => 13 => 11 => 11 => 4 => 4 => 10 => 10 => 1 => 1

        # iterate through the merged list
        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next


        curr = head
        newHead = head.next
        newcurr = newHead

        while curr:
            curr.next = newcurr.next
            curr = curr.next
            if curr:
                newcurr.next = curr.next
                newcurr = newcurr.next
        return newHead

        
            



        