class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        ancestorList = []
        for u, v in edges:
            adj[v].append(u)
        def dfs(start, visited):
            visited[start] = 1
            for neigh in adj[start]:
                if not visited[neigh]:
                    dfs(neigh, visited)
        for i in range(n):
            visited = [0] * n
            ancestors = []
            dfs(i, visited)

            for j in range(n):
                if j == i:
                    continue
                if visited[j]:
                    ancestors.append(j)

            ancestorList.append(ancestors)

        return ancestorList