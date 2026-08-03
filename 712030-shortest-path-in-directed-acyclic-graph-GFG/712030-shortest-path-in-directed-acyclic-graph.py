from typing import List
from collections import deque, defaultdict

class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        
        adj_list = defaultdict(list)
        topo_sort = []
        visited = set()
        distance = [float('inf')] * V
        src = 0
        for u,v,wt in edges:
            adj_list[u].append([v, wt])
        
        
        def topoSort(node):
            nonlocal topo_sort
            if node in visited:
                return 
            visited.add(node)
            for neigh, wt in adj_list[node]:
                topoSort(neigh)
            
            topo_sort.append(node)
        
        topoSort(src)
        
        topo_sort = list(reversed(topo_sort))
        distance[src] = 0
        
        for node in topo_sort:
            dist = distance[node]
            for neigh,wt in adj_list[node]:
                distance[neigh] = min(distance[neigh], dist + wt)
        
        for i in range(V):
            if distance[i] == float("inf"):
                distance[i] = -1
                
        return distance
        
        
        
        
            
            
                
            
            
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna