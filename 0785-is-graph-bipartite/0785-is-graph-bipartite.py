class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        group = [-1] * n

        def bfs(start, pg):
            queue = deque()
            queue.append(start)
            group[start] = "A"

            while queue:
                node = queue.popleft()
                for neigh in graph[node]:
                    if group[neigh] == -1:
                        group[neigh] = "A" if group[node] == "B" else "B"
                        queue.append(neigh)
                    else:
                        if group[neigh] == group[node]:
                            return False
            
            return True
        for i in range(n):
            if group[i] == -1:
                if not bfs(i, "A"):
                    return False

        return True
        