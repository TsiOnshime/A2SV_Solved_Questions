#User function Template for python3

from typing import List
from collections import deque

class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        
        res = [float('inf')] * V
        res[0] = 0
        indegree = [0] * V
        queue = deque()
        adj = {c : [] for c in range(V)}
        top_order = []
        
        for i in range(E):
            u, v, dist = edges[i]
            adj[u].append([v, dist])
            indegree[v] += 1
            
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            node = queue.popleft()
            top_order.append(node)
            for curr_neigh in adj[node]:
                neigh, dist = curr_neigh
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
                    
        for node in top_order:
            if res[node] != float('inf'):
                for edg in adj[node]:
                    neigh, dist = edg
                    new_dist = res[node] + dist
                    res[neigh] = min(res[neigh], new_dist)
        
        for i in range(len(res)):
            if res[i] == float('inf'):
                res[i] = -1
                
        return res
            
        
        
            
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna