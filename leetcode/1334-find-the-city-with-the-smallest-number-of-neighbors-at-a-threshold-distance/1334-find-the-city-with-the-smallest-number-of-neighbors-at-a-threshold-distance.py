class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance = [[float('inf')] * n for i in range(n)]
        adj_list = defaultdict(list)

        for u, v, wt in edges:
            adj_list[u].append([v, wt])
            adj_list[v].append([u, wt])

        
        for i in range(n):
            distance[i][i] = 0

        for k in range(n):
            min_heap = []
            heapq.heappush(min_heap, [0, k])
            distance[k][k] = 0
            while min_heap:
                dist, node = heapq.heappop(min_heap)
                if dist > distance[k][node]:
                    continue
                for neigh, d in adj_list[node]: 
                    if dist + d < distance[k][neigh]:
                        distance[k][neigh] = dist + d
                        heapq.heappush(min_heap, [dist + d, neigh])
        
       
        city = -1
        min_count = float('inf')
        
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and distance[i][j] <= distanceThreshold:
                    count += 1
            
            if count <= min_count:
                city = i
                min_count = count
        return city

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna