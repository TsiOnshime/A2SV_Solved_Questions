class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[[float('-inf')] * cols for i in range(cols)] for j in range(rows)]
   
        def pickUp(i, j1, j2):
            if j1 < 0 or j2 < 0 or j1 >= cols or j2 >= cols:
                return float('-inf')
            if i == rows - 1:
                if j1 == j2:
                    return grid[i][j1]
                return grid[i][j1] + grid[i][j2]
            
            if dp[i][j1][j2] != float('-inf'):
                return dp[i][j1][j2]

            _max = float('-inf')
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if j1 == j2:
                        _max = max(_max, grid[i][j1] + pickUp(i + 1, j1 + x, j2 + y))
                    else:
                        _max = max(_max, grid[i][j1] + grid[i][j2] + pickUp(i + 1, j1 + x, j2 + y))
            dp[i][j1][j2] = _max
            return _max

        return pickUp(0, 0, cols - 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna