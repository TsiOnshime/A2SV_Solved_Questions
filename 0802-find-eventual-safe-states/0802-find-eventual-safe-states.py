class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [False] * n
        colour = [0] * n
        safe_nodes = []

        
                

        def dfs(node):
            if colour[node] == 1:
                return False
            if colour[node] == 2:
                return True
            colour[node] = 1
            
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            
            colour[node] = 2
            safe[node] = True
            return True

        for i in range(n):
            if colour[i] == 0:
                dfs(i)
        for i in range(n):
            if safe[i] == True:
                safe_nodes.append(i)
        return safe_nodes