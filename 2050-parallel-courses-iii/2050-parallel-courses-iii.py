class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        indegree = [0] * (n + 1)
        sTime = [0] * (n + 1) # max stopping time of each course
        queue = deque()
        for u, v in relations:
            adj[u].append(v)
            indegree[v] += 1
        for i in range(1, len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        for i in range(len(queue)):
            sTime[queue[i]] = time[queue[i] - 1]

        while queue:
            node = queue.popleft()
            for neigh in adj[node]:
                sTime[neigh] = max(sTime[neigh], time[neigh - 1] + sTime[node])
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        return max(sTime)