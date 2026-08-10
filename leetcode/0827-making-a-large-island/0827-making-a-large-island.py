class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return 
        if self.size[parent1] > self.size[parent2]:
            self.parent[parent2] = parent1
            self.size[parent1] += self.size[parent2]
        else:
            self.parent[parent1] = parent2
            self.size[parent2] += self.size[parent1]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        max_size = 1
        uf = UnionFind(rows * cols)

        def is_valid(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                return True
            return False

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    node = r * cols + c
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if is_valid(nr, nc):
                            neigh = nr * cols + nc
                            uf.union(node, neigh)
        
        for r in range(rows):
            for c in range(cols):
                visited = set()
                if grid[r][c] == 0:
                    size = 1
                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c
                        if is_valid(nr, nc):
                            visited.add(uf.find(nr * cols + nc))
                    for i in visited:
                        size += uf.size[i]
                
                    max_size = max(size, max_size)
        return max(max(uf.size), max_size)



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna