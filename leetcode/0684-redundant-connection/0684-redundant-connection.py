class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # I'll go through the edges connecting them if they are already connected I'd set the ans to be that edge and return 
        n = len(edges)
        parent = [i for i in range(n)]
        rank = [0] * n
        res = []
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        def union(u, v):
            nonlocal res
            p1, p2 = find(u), find(v)

            if p1 == p2:
                res = [u + 1, v + 1]
                return 

            if rank[p1] == rank[p2]:
                parent[p1] = p2
                rank[p2] += 1
            elif rank[p1] > rank[p2]:
                parent[p2] = p1
            else:
                parent[p1] = p2

        for u, v in edges:
            union(u - 1, v - 1)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna