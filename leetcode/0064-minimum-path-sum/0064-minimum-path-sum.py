class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        rows, cols = len(grid), len(grid[0])
        def minPath(r, c):
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]
            if (r, c) in memo:
                return memo[(r, c)]
            
            right = minPath(r, c + 1) if c + 1 < cols else float("INF")
            down = minPath(r + 1, c) if r + 1 < rows else float("INF")

            memo[(r, c)] = min(down, right) + grid[r][c]
            return min(down, right) + grid[r][c]
        return minPath(0, 0)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna