class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    self.explore(r, c, visited, rows, cols, directions, grid)
                    count += 1
        return count

    def is_valid(self, r, c, visited, rows, cols, grid):
        if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == "1":
            return True
        return False
    
    def explore(self, r, c, visited, rows, cols, directions, grid):
        if not self.is_valid(r, c, visited, rows, cols, grid):
            return 
        visited.add((r, c))
        for dr, dc in directions:
            self.explore(r + dr, c + dc, visited, rows, cols, directions, grid)
            



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna