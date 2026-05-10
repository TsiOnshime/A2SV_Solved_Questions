class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = deque()
        visited = set()
        minutes = 0


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))

        if fresh == 0:
            return 0

        def is_valid(r, c):
            if r in range(rows) and c in range(cols) and (r, c) not in visited and grid[r][c] == 1:
                return True
            return False

        while queue:
            n = len(queue)
            for _ in range(n):
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + cr, dc + cc
                    if is_valid(nr, nc):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        fresh -= 1
            minutes += 1
   
        return minutes - 1 if fresh == 0 else -1