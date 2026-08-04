class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        if grid[0][0] != 0:
            return -1
            
        def is_valid(r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0 and (r, c) not in visited:
                return True
            return False
        queue.append((0, 0, 1))
        visited.add((0, 0))

        while queue:
            r, c, pathLen = queue.popleft()
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return pathLen
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc):
                    queue.append([nr, nc, pathLen + 1])
                    visited.add((nr, nc))

        return -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna