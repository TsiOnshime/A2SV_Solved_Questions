class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        queue = deque()
        queue.append([0])
        target = len(graph) - 1
        res = []

        while queue:
            path = queue.popleft()

            if path[-1] == target:
                res.append(path.copy())
                continue
            for neigh in graph[path[-1]]:
                queue.append(path + [neigh])
        
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna