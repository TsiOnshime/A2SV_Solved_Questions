class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        count = 0

        def dfs(city1):
            if city1 in visited:
                return 0
            visited.add(city1)

            for city2 in range(n):
                if isConnected[city1][city2] == 1 and city2 not in visited:
                    dfs(city2)
            return 1
        for city in range(n):
            count += dfs(city)
        
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna