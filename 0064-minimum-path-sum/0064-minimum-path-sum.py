class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        for c in range(cols-2,-1,-1):
            grid[rows-1][c] += grid[rows-1][c + 1]
        
        for r in range(rows - 2, -1, -1):
            for c in range(cols - 1, -1, -1):
                down = grid[r + 1][c] if r + 1 < rows else float('inf')
                right = grid[r][c + 1] if c + 1 < cols else float('inf')
                grid[r][c] = grid[r][c] + min(down, right)

        return grid[0][0]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna