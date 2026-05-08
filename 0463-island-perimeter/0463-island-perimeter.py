class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def is_valid(r, c, visited, peri):
        
            if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visited:
                return True
            

                
        def bfs(r, c):
            visited = set()
            queue = deque()
            count = 0

            queue.append((r, c))
            visited.add((r, c))
            while queue:
                peri = 4
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if is_valid(nr, nc, visited, peri):
                        queue.append((nr, nc))
                        visited.add((nr,nc))
                        peri -= 1
                    elif (nr,nc) in visited:
                        peri -= 1
                    
                count += peri
            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return bfs(r, c)
                