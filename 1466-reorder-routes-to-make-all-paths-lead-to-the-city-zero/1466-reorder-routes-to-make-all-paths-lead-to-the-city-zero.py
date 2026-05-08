class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = {c: [] for c in range(n)}
        queue = deque()
        visited = set()
        count = 0
        for u, v in connections:
            adj[u].append([v, 1])
            adj[v].append([u, 0])

        def dfs(node, sign):
            nonlocal count
            if node in visited:
                return 0
            count += sign
            visited.add(node)
            for [neigh, sign] in adj[node]:
                dfs(neigh, sign)
        dfs(0, 0)
        return count





