"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        stack = []
        dummy = Node(0, None, head, [])

        while head:
            if head.child:
                temp = head.next
                head.next = head.child
                head.child.prev = head
                head.child = None
                if temp:
                    stack.append(temp)
            if head.next == None and stack:
                head.next = stack.pop()
                head.next.prev = head

            head = head.next

        return dummy.next



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna