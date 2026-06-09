"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        while curr:
            dummy = Node()
            temp = dummy 
            while curr:
                if curr.left:
                    temp.next = curr.left
                    temp = temp.next
                if curr.right:
                    temp.next = curr.right
                    temp = temp.next
                curr = curr.next
            curr = dummy.next

        return root

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna