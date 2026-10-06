from collections import defaultdict
class Solution:
    def graphColoring(self, v, edges, m):
        if m == 0:
            return False
        colours = [0] * v
        adj_list = defaultdict(list)
        for u, w in edges:
            adj_list[u].append(w)
            adj_list[w].append(u)
        
        def is_possible(n, col):
            for i in adj_list[n]:
                if colours[i] == col:
                    return False
            return True
        
        def solve(node):
            if node == v:
                return True
            
            for i in range(1, m + 1):
                if is_possible(node, i):
                    colours[node] = i
                    if solve(node + 1):
                        return True
                    colours[node] = 0
            return False
        
        return solve(0)
                    
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna