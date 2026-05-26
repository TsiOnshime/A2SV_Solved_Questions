class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows, cols = len(isConnected), len(isConnected[0])
        parent = [i for i in range(rows)]
        rank = [0] * rows

        def find(node):

            while node != parent[node]:
                parent[node] = find(parent[node])
                node = parent[node]
            return node

        
        def union(a, b):
            p1, p2 = find(a), find(b)

            if p1 == p2:
                return 0

            if rank[p1] == rank[p2]:
                parent[p1] = p2
                rank[p2] += 1
            elif rank[p1] > rank[p2]:
                parent[p2] = p1
            else:
                parent[p1] = p2

            return 1
        provinces = rows
        for r in range(rows):
            for c in range(cols):
                if isConnected[r][c] == 1:
                    provinces -= union(r, c)

        return provinces
        





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna