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
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(28)
        offset = 97
        for eq in equations:
            chr1, chr2 = eq[0], eq[-1]
            comparator = eq[1:3]
            if comparator == "==":
                u = ord(chr1) - offset
                v = ord(chr2) - offset
                uf.union(u, v)

        for eq in equations:
            chr1, chr2 = eq[0], eq[-1]
            comparator = eq[1:3]
            if comparator == "!=":
                u = ord(chr1) - offset
                v = ord(chr2) - offset
                if uf.find(u) == uf.find(v):
                    return False
        return True


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna