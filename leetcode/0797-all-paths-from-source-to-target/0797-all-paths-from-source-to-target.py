class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path =[]
        res = []
        target = len(graph) - 1
        def get_candidates(i):
            return graph[i]
        def is_valid(node):
            if node == target:
                return True
            return False
        def search(src, node):
            if is_valid(node):
                path.append(node)
                res.append(path.copy())
                return
            # [0,1]
            path.append(node)
            for candidate in get_candidates(node):
                search(src, candidate)
                path.pop()
        search(0, 0)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna