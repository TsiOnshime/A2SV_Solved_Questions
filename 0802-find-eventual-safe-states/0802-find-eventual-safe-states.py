class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = {c: [] for c in range(n)}
        queue = deque()
        safe = [False] * n
        indegree = [0] * n
        safe_nodes = []

        for u in range(len(graph)):
            for v in graph[u]:
                adj[v].append(u)
                indegree[u] += 1

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            safe[node] = True
            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)

        for i in range(n):
            if safe[i] == True:
                safe_nodes.append(i)

        return safe_nodes
                
        