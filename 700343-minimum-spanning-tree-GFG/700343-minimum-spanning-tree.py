import heapq
from collections import defaultdict

class UnionFind:
    def __init__(self, V):
        self.rank = [0] * V
        self.parent = [i for i in range(V)]
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        
        if parent1 == parent2:
            return False
        
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        elif self.rank[parent2] > self.rank[parent1]:
            self.parent[parent1] = parent2
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += 1
            
        return True
        
        
class Solution:
    def spanningTree(self, V: int, edges: list[list[int]]) -> int:
       
        edges.sort(key=lambda x: x[2])
        
        uf = UnionFind(V)
        
        _sum = 0
        edges_used = 0
        for u, v, wt in edges:
            if uf.union(u, v):
                _sum += wt
                edges_used += 1
                if edges_used == V - 1:
                    break
        return _sum
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna