class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = set()
        queue = deque()

        def is_valid(r, c):
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == 1:
                return True
            return False
        def bfs(r, c):
            queue.append((r, c))
            visited.add((r, c))
            peri = 0

            while queue:
                cr, cc = queue.popleft() 
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if is_valid(nr, nc):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                    else:
                        if (nr, nc) not in visited:
                            peri += 1

            return peri
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return bfs(r, c)
