class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        fresh = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        minute = 0
        while queue:
            n = len(queue)
            for i in range(n):
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if nr < 0 or nr == rows or nc < 0 or nc == cols or (nr, nc) in visited or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    queue.append((nr, nc))
                    visited.add((nr, nc))
                    fresh -= 1
            minute += 1
        
        if fresh > 0:
            return -1
        return max(0, minute - 1)

