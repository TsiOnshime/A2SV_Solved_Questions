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
            return True
        self.components -= 1
        if self.rank[p1] == self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p2] += 1
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
        return False
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        bob = UnionFind(n)
        alice = UnionFind(n)
        remove = 0
        edges.sort(reverse = True)
        for edge in edges:
            typ, u, v = edge
            if typ == 3:
                b = bob.union(u - 1, v - 1)
                a = alice.union(u - 1, v - 1)

                if b and a:
                    remove += 1

            elif typ == 2:
                if bob.union(u - 1, v - 1):
                    remove += 1
            else:
                if alice.union(u - 1, v - 1):
                    remove += 1

        if bob.components != 1 or alice.components != 1:
            return -1
        return remove

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna