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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        queue = deque()
        queue.append(root)

        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if i != n - 1 and queue:
                    node.next = queue[0]
                for neigh in [node.left, node.right]:
                    if neigh:
                        queue.append(neigh)
        
        return root
        



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna