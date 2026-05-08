class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = {c: [] for c in range(n)}
        queue = deque()
        visited = set()

        for u, v in connections:
            adj[u].append([v, 1])
            adj[v].append([u, 0])

        queue.append(0)
        visited.add(0)
        count = 0
        while queue:
            node = queue.popleft()
            for [neigh, sign] in adj[node]:
                if neigh not in visited:
                    count += sign
                    queue.append(neigh)
                    visited.add(neigh)

        return count



