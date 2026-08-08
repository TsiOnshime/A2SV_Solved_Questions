class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)

        if parent1 == parent2:
            return False
        
        if self.rank[parent1] < self.rank[parent2]:
            self.parent[parent1] = parent2
        elif self.rank[parent2] < self.rank[parent1]:
            self.parent[parent2] = parent1
        else:
            self.parent[parent2] = parent1
            self.rank[parent1] = parent2
        
        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        provinces = n

        uf = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j] == 1 and uf.union(i, j):
                    provinces -= 1

        return provinces

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna