class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        indegree = [0] * n
        ancestorList = [set() for i in range(n)]
        queue = deque()

        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1


        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
    
        for node in order:
            for neigh in adj[node]:
                ancestorList[neigh].add(node)
                ancestorList[neigh].update(ancestorList[node])

        for i in range(len(ancestorList)):
            ancestorList[i] = list(sorted(ancestorList[i]))

        return ancestorList

        