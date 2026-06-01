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
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)

        edgeList.sort(key = lambda x: x[2])

        q = [[l, p, q, i] for i, [p, q, l] in enumerate(queries)]
        q.sort()
        m = len(queries)
        ans = [False] * m

        edge_idx = 0
        edge_size = len(edgeList)

        for dist, p, q, i in q:
  
            while edge_idx < edge_size and edgeList[edge_idx][2] < dist:         
                u, v = edgeList[edge_idx][0], edgeList[edge_idx][1]
                uf.union(u, v)
                edge_idx += 1
               
            p1, p2 = uf.find(p), uf.find(q)

            ans[i] = p1 == p2

        return ans

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna