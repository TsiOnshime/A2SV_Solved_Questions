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
            return 
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        elif self.rank[parent2] > self.rank[parent1]:
            self.parent[parent1] = parent2
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += 1        
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows, cols = 0, 0
        for u,v in stones:
            rows = max(rows, u)
            cols = max(cols, v)

        offset = rows + 1

        n = offset + cols + 1
        stone_nodes = defaultdict(int)
        components = 0
        
        uf = UnionFind(n)

        for r, c in stones:
            uf.union(r, c + offset)
            stone_nodes[r] = 1
            stone_nodes[c + offset] = 1


        for node in stone_nodes.keys():
            if uf.find(node) == node:
                components += 1
        return len(stones) - components


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna