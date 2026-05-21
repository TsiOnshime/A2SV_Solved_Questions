class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        n = len(equations)
        res = []
        for i in range(n):
            u, v = equations[i]
            graph[u].append([v, values[i]])
            graph[v].append([u, 1/values[i]])
        def bfs(start, finish):
            if start not in graph or finish not in graph:
                return -1
            queue, visited = deque(), set()
            queue.append([start, 1])
            visited.add(start)

            while queue:
                node, weight = queue.popleft()
                if node == finish:
                    return weight
                for elem, val in graph[node]:
                    if elem not in visited:
                        queue.append([elem, weight * val])
                        visited.add(elem)
            return -1
        for u, v in queries:
            output = bfs(u, v)
            res.append(output)

        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna