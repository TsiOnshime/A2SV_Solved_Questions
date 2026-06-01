class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.components = n
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, u, v):
        p1, p2 = self.find(u), self.find(v)
        if p1 == p2:
            return 
        self.components -= 1
        if self.rank[p1] == self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p2] += 1
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n) # type 1
        bob = UnionFind(n) # type 2
        edges.sort(reverse=True)
        res = 0
        edge_size = len(edges)
        edge_idx = 0
        while edge_idx < edge_size and edges[edge_idx][0] == 3: 
            u, v = edges[edge_idx][1], edges[edge_idx][2]
            p1, p2 = alice.find(u - 1), alice.find(v - 1)
            if p1 == p2:
                res += 1
            else:
                alice.union(u - 1, v - 1)
                bob.union(u - 1, v - 1)
            edge_idx += 1
        
        while edge_idx < edge_size and edges[edge_idx][0] == 2:
            u, v = edges[edge_idx][1], edges[edge_idx][2]
            p1, p2 = bob.find(u - 1), bob.find(v - 1)
            if p1 == p2:
                res += 1
            else:
                bob.union(u - 1, v - 1)
            edge_idx += 1

        while edge_idx < edge_size and edges[edge_idx][0] == 1:
            u, v = edges[edge_idx][1], edges[edge_idx][2]
            p1, p2 = alice.find(u - 1), alice.find(v - 1)
            if p1 == p2:
                res += 1
            else:
                alice.union(u - 1, v - 1)
            edge_idx += 1


        if bob.components != 1 or alice.components != 1:
            return -1
        
        return res

        



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna