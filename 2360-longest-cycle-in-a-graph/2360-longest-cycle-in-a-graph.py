class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        max_length = -1
        visited = [0] * len(edges)
        pathVisited = [0] * len(edges)

        def findLongestCycle(node):
            nonlocal max_length
            visited[node] = 1
            pathVisited[node] = 1
            neigh = edges[node]
            if neigh == -1:
                pathVisited[node] = 0
                return 
            if visited[neigh] and pathVisited[neigh]:
                return [1, neigh]
            if visited[neigh] == 0:
                res = findLongestCycle(neigh)
                if not res:
                    return 
                length, starting_node = res
                if starting_node == node:
                    max_length = max(max_length, length + 1)
                    return 
                else:
                    return [length + 1, starting_node]
            pathVisited[node] = 0
        
        for i in range(len(edges)):
            if visited[i] == 0:
                findLongestCycle(i)

        return max_length

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna