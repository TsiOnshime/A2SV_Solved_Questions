from collections import defaultdict

class Solution:
    def isCyclic(self, V, edges):
        adj_list = defaultdict(list)
        visited = [0] * V
        pathVisited = [0] * V
        
        for u, v in edges:
            adj_list[u].append(v)
            
        
        def detectCycle(node):
            
            for neigh in adj_list[node]:
                if visited[neigh] == 0:
                    visited[neigh] = 1
                    pathVisited[neigh] = 1
                    if detectCycle(neigh):
                        return True
                    
                elif pathVisited[neigh]:
                    return True
            pathVisited[node] = 0
            return False
  
        for i in range(V):
            if visited[i] == 0:
                visited[i] = 1
                pathVisited[i] = 1
                if detectCycle(i):
                    return True
        return False
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna