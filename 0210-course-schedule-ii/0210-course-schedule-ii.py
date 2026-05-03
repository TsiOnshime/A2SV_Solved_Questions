class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        queue = deque()
        indegree = [0] * numCourses
        pathVisited = [0] * numCourses
        visited = [0] * numCourses
        adj = defaultdict(list)

        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1

        def detectCycle(start):
            visited[start] = 1
            pathVisited[start] = 1

            for neigh in adj[start]:
                if not visited[neigh]:
                    if detectCycle(neigh):
                        return True
            
                else:
                    if pathVisited[neigh]:
                        return True
            pathVisited[start] = 0
            return False
            


        for i in range(numCourses):
            if not visited[i]:
                cycle = detectCycle(i)

                if cycle:
                    return []

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            order.append(node)
            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)

        return order
