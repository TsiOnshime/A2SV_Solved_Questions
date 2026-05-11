class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()

        def bfs(start):
            queue = deque()
            queue.append(start)
        

            group = {start: "A"}

            while queue:
                node = queue.popleft()
                for neigh in graph[node]:
                    if neigh not in group:
                        if group[node] == "A": group[neigh] = "B"
                        else: group[neigh] = "A"
                        queue.append(neigh)
                    else:

                        if group[node] == group[neigh]:
                            return False
            return True

        truth = True
        for i in range(len(graph)):
            if len(graph[i]) > 0 and i not in visited:
                truth = truth and bfs(i)
                if not truth:
                    return False
        return True