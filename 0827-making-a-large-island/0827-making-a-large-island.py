class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        marker_area = {}
        marker = 2
        max_area = 0

        def dfs(r, c, marker):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0
            

            grid[r][c] = marker
            left = dfs(r, c - 1, marker)
            right = dfs(r, c + 1, marker)
            up = dfs(r - 1, c, marker)
            down = dfs(r + 1, c, marker)

            return 1 + left + right + up + down
       

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    size = dfs(r, c, marker)
                    marker_area[marker] = size
                    max_area = max(max_area, size)
                    marker += 1
        
        for r in range(rows):
            for c in range(cols):
                markers_connected = set()
                area = 1
                if grid[r][c] == 0:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 0 and grid[nr][nc] not in markers_connected:
                            area += marker_area[grid[nr][nc]]
                            markers_connected.add(grid[nr][nc])
                    
                    max_area = max(max_area, area)
        return max_area





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna