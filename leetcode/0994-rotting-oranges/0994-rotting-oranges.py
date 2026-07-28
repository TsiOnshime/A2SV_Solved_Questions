class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        queue = deque()
        visited = set()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
      
        def is_valid(r, c):
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == 1:
                return True
            return False
        
        def bfs():
            nonlocal fresh
            minute = 0
            while queue:
                n = len(queue)
                for i in range(n):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c
                        if is_valid(nr, nc):
                            queue.append((nr, nc))
                            visited.add((nr, nc))
                            fresh -= 1
                            
                minute += 1
            
            return minute - 1


        minutes = bfs()
        return minutes if fresh == 0 else -1
       


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna