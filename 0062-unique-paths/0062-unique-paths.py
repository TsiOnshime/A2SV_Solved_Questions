class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0] * n for i in range(m)]
        print(paths)
        for i in range(m):
            paths[i][0] = 1
        for j in range(n):
            paths[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
        return paths[m - 1][n - 1]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna