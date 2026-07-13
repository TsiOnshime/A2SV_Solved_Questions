class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols= len(grid), len(grid[0])
        count = 0
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        def is_valid(r, c):
            if 0 <= r < rows  and 0 <= c < cols and grid[r][c] == 0 and (r, c) not in visited:
                return True
            return False

        def dfs(r, c):
            nonlocal closed
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                closed = False
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if is_valid(nr, nc):
                    visited.add((nr, nc))
                    dfs(nr,nc)
            return closed
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r, c) not in visited:
                    closed = True
                    visited.add((r, c))
                    if dfs(r, c):
                        count += 1
        return count




        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna