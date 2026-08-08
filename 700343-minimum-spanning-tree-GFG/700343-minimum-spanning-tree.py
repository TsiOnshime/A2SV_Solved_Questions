import heapq
from collections import defaultdict
class Solution:
    def spanningTree(self, V: int, edges: list[list[int]]) -> int:
        # code here
        _sum = 0
        adj_list = defaultdict(list)
        
        for u, v, wt in edges:
            adj_list[u].append([v, wt])
            adj_list[v].append([u, wt])
        
        # wt, node
        min_heap = []
        heapq.heappush(min_heap, [0, 0])
        
        visited = set()
        
        while min_heap:
            wt, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            _sum += wt
            visited.add(node)
            for neigh, dist in adj_list[node]:
                if neigh not in visited:
                    heapq.heappush(min_heap, [dist, neigh])
                    
        return _sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna