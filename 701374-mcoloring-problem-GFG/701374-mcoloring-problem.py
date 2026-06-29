from collections import defaultdict
class Solution:
    def graphColoring(self, v, edges, m):
        # code here
        adj_list = defaultdict(list)
        node_colour = [0] * v
        for u, w in edges:
            adj_list[u].append(w)
            adj_list[w].append(u)
        
        def possible(node, c):
            for neigh in adj_list[node]:
                if node_colour[neigh] == c:
                    return False
            return True
        def colouring(node):
            if node == v:
                return True
            
            for c in range(1, m + 1):
                if possible(node, c):
                    node_colour[node] = c
                    if colouring(node + 1):
                        return True
                    node_colour[node] = 0
            
            return False
            
        return colouring(0)
            
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna