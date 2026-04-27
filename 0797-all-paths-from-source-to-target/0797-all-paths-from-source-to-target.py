class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def dfs(start, dest, path):
            path.append(start)
            if start == dest:
                res.append(path.copy())

            else:
                for neigh in graph[start]:
                    dfs(neigh, dest, path)

            path.pop()

        dfs(0, len(graph) - 1, [])
        return res