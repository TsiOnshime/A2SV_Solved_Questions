class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def is_valid(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited:
                return True
            return False
        def bfs(r, c):
            queue = deque()
            queue.append([r, c])
            visited.add((r, c))
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, c + dc
                    if is_valid(nr, nc):
                        queue.append([nr, nc])
                        visited.add((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    bfs(r, c)
        
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna