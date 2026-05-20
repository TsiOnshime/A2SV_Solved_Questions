class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    self.explore(r, c, visited, directions, rows, cols, grid)
                    count += 1

        return count

    def is_valid(self, r, c, rows, cols, visited, grid):
        if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == "1": 
            return True
        return False


    def explore(self, r, c, visited, directions, rows, cols, grid):
        visited.add((r, c))
        queue = deque()
        queue.append([r, c])

        while queue:
            cr, cc = queue.popleft()
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if self.is_valid(nr, nc, rows, cols, visited, grid):
                    queue.append([nr, nc])
                    visited.add((nr, nc))






# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna