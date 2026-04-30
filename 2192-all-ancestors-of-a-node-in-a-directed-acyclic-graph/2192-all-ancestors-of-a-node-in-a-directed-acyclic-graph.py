class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_list = defaultdict(list)
        ancestor_list = [set() for i in range(n)]

        for u, v in edges:
            adj_list[u].append(v)

        def bfs(start):
            queue = deque()
            visited = set()
            queue.append(start)
            visited.add(start)

            while queue:
                node = queue.popleft()
                for neigh in adj_list[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)
                        ancestor_list[neigh].add(start)
                

        for i in range(n):
            bfs(i)
        
        return [sorted(list(s)) for s in ancestor_list]

        