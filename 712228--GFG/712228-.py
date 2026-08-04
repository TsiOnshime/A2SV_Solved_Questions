import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, V, edges, src, dest):

        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # --------------------
        # Dijkstra
        # --------------------

        INF = float("inf")
        dist = [INF] * (V + 1)
        dist[src] = 0

        pq = [(0, src)]

        while pq:
            d, node = heapq.heappop(pq)

            if d > dist[node]:
                continue

            for neigh, wt in adj[node]:
                nd = d + wt

                if nd < dist[neigh]:
                    dist[neigh] = nd
                    heapq.heappush(pq, (nd, neigh))

        if dist[dest] == INF:
            return [-1]

        # --------------------
        # Build shortest path DAG
        # --------------------

        dag = defaultdict(list)

        for u, v, w in edges:

            if dist[u] + w == dist[v]:
                dag[u].append(v)

            if dist[v] + w == dist[u]:
                dag[v].append(u)

        for node in dag:
            dag[node].sort()

        # --------------------
        # DFS
        # --------------------

        path = []

        def dfs(node):
            path.append(node)

            if node == dest:
                return True

            for neigh in dag[node]:
                if dfs(neigh):
                    return True

            path.pop()
            return False

        dfs(src)

        return path

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna