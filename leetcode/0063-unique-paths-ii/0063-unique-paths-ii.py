class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # how many possible paths are there from (i, j) to (m - 1, n - 1)
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        def path(i, j):
            if i >= m or j >= n:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]
            val = path(i + 1, j) + path(i, j + 1)

            memo[i][j] = val
            return val

        memo = [[-1] * n for i in range(m)]

        return path(0, 0)



        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna