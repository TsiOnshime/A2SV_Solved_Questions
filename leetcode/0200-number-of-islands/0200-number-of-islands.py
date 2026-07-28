class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def is_valid(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited:
                return True
            return False
        def dfs(r, c):
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if is_valid(nr, nc):
                    dfs(nr, nc)
            
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    number_of_islands += 1
        
        return number_of_islands

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna