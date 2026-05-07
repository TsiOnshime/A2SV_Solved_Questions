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
        oldNew = {}

        queue = deque()
        queue.append(node)
        visited = set()
        visited.add(node)
        while queue:
            curr = queue.popleft()
            oldNew[curr] = Node(curr.val)
            
            for neigh in curr.neighbors:
                if neigh and neigh not in visited:
                    queue.append(neigh)
                    visited.add(neigh)
        for old, new in oldNew.items():
            for neigh in old.neighbors:
                new.neighbors.append(oldNew[neigh])
        return oldNew[node]