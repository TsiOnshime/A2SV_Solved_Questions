class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, u, v):
        p1, p2 = self.find(u), self.find(v)

        if p1 == p2:
            return 
        
        if self.rank[p1] == self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p2] += 1
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
    
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        max_row = 0
        max_col = 0
        for u, v in stones:
            max_row = max(max_row, u)
            max_col = max(max_col, v)

        n = max_row + max_col + 2
        # [0, 1, 2, 3, 4, 5, 6]
        uf = UnionFind(n)
        used = set()
        def get_new_idx(c):
            return c + max_row + 1
        for u, v in stones:
            new_col = get_new_idx(v)
            uf.union(u, new_col)
            used.add(u)
            used.add(new_col)

        roots = set()
        for i in used:
            roots.add(uf.find(i))

        return len(stones) - len(roots)
        

        


# from each connected component spare one element



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna