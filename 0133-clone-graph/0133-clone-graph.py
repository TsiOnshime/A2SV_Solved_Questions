"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        
        old_new = {node: Node(node.val)}

        queue = deque()
        queue.append(node)

        while queue:
            curr = queue.popleft()
            for neigh in curr.neighbors:
                if neigh not in old_new:
                    old_new[neigh] = Node(neigh.val)
                    queue.append(neigh)
                old_new[curr].neighbors.append(old_new[neigh])
        return old_new[node]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna