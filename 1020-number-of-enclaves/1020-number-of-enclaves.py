class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        queue = deque()

        def bfs(r, c):
            if grid[r][c] == 0:
                return 
            queue.append([r, c])
            visited.add(tuple([r, c]))

            while queue:
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited and grid[nr][nc] == 1:
                        queue.append([nr, nc])
                        visited.add(tuple([nr, nc]))

        for i in range(cols):
            bfs(0, i)
            bfs(rows - 1, i)

        for i in range(rows):
            bfs(i, 0)
            bfs(i, cols - 1)
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    count += 1

        return count