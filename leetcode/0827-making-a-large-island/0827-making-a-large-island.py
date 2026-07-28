class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = set()
        rows, cols = len(grid), len(grid[0])
        marker_area = {}
        marker = 2
        max_area = 0

        
        def is_valid(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                return True
            return False

        def dfs(r, c, marker):
            nonlocal size
            size += 1
            grid[r][c] = marker
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if is_valid(nr, nc):
                    dfs(nr, nc, marker)
       

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    size = 0
                    dfs(r, c, marker)
                    marker_area[marker] = size
                    marker += 1
        
        for r in range(rows):
            for c in range(cols):
                markers_connected = set()
                area = 1
                if grid[r][c] == 0:
                    if r - 1 >= 0 and grid[r-1][c] != 0 and grid[r-1][c] not in markers_connected:
                        area += marker_area[grid[r-1][c]]
                        markers_connected.add(grid[r-1][c])
                    if r + 1 < rows and grid[r + 1][c] != 0 and grid[r + 1][c] not in markers_connected:
                        area += marker_area[grid[r + 1][c]]
                        markers_connected.add(grid[r + 1][c])
                    if c - 1 >= 0 and grid[r][c - 1] != 0 and grid[r][c - 1] not in markers_connected:
                        area += marker_area[grid[r][c - 1]]
                        markers_connected.add(grid[r][c - 1])
                    if c + 1 < cols and grid[r][c + 1] != 0 and grid[r][c + 1] not in markers_connected:
                        area += marker_area[grid[r][c + 1]]
                        markers_connected.add(grid[r][c + 1])
                    
                    max_area = max(max_area, area)
        for mark, area in marker_area.items():
            max_area = max(area,  max_area)

        return max_area





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna