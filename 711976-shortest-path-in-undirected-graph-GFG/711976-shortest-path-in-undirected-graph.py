from collections import deque
class Solution:
    def buildGraph(self, V, edges):
        adj = {c: [] for c in range(V)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        return adj
        
    def shortestPath(self, V, edges, src):
        graph = self.buildGraph(V, edges)
        
        res = [-1] * V
        res[src] = 0
        visited = {src}
        queue = deque()
        queue.append([src, 0])
        
        while queue:
            node, dist = queue.popleft()
            if res[node] != float('inf'):
                for neigh in graph[node]:
                    if neigh not in visited:
                        new_dist = dist + 1
                        res[neigh] = new_dist
                        queue.append([neigh, new_dist])
                        visited.add(neigh)
                        
       
                
        return res
        
        
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna