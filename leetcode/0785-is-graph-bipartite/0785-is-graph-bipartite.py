class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        group = [-1] * n

        def bfs(node):
            queue = deque()
            group[node] = 0
            queue.append(node)
            while queue:
                node = queue.popleft()
                for neigh in graph[node]:
                    if group[neigh] == -1:
                        group[neigh] = not group[node]
                        queue.append(neigh)
                    elif group[neigh] == group[node]:
                        return False

            return True

        for i in range(n):
            if group[i] == -1:
                if not bfs(i):
                    return False

        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna