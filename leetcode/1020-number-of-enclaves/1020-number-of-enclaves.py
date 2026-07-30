class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or (r, c) in visited or grid[r][c] == 0:
                return
            visited.add((r, c))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    count += 1

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna