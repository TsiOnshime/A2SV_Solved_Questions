class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        queue = deque()
        order = []
        adj = {c:[] for c in range(numCourses)}

        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        
    
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
            

        return order if len(order) == numCourses else []
