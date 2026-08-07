class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance = [[float('inf')] * n for i in range(n)]
        
        for u, v, wt in edges:
            distance[u][v] = wt
            distance[v][u] = wt

        
        for i in range(n):
            distance[i][i] = 0

        for k in range(n):
            for src in range(n):
                for dest in range(n):
                    if distance[src][k] != float('inf') and distance[k][dest] != float('inf'):
                        distance[src][dest] = min(distance[src][dest], distance[src][k] + distance[k][dest])
        

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