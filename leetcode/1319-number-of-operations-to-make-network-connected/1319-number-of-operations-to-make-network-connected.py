class UnionFind:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [i for i in range(n)]
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)

        if parent1 == parent2:
            return [1, 0]
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent1] = parent2
        elif self.rank[parent2] > self.rank[parent1]:
            self.parent[parent2] = parent1
        else:
            self.parent[parent2] = parent1
            self.rank[parent1] += 1
        return [0, 1]
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        extra_cable = 0
        components = n
        uf = UnionFind(n)

        for u, v in  connections:
            cable, component = uf.union(u, v)
            
            extra_cable += cable
            components -= component

        return components - 1 if extra_cable >= components-1 else -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna