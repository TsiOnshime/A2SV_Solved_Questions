class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_ordering = []
        adj_list = defaultdict(list)
        queue = deque()
        indegree = [0] * numCourses
        
        for u, v in prerequisites:
            adj_list[v].append(u)
            indegree[u] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            course_ordering.append(node)
            for neigh in adj_list[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        
        return course_ordering if len(course_ordering) == numCourses else []



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna