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
        # [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
        n = len(stones)
        uf = UnionFind(n)
        for i in range(n - 1):
            for j in range(i + 1, n):
                u = stones[i]
                v = stones[j]
                if u[0] == v[0] or u[1] == v[1]:
                    uf.union(i, j)
        roots = set()

        for i in range(n):
            roots.add(uf.find(i))

        return n - len(roots)
        

        


# from each connected component spare one element



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna