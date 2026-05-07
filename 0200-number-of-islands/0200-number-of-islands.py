class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
       
        def is_valid(r, c):
            if 0 <= r < rows and 0<= c < cols and (r, c) not in visited and grid[r][c] == "1":
                return True
            return False

        def bfs(start, visited):
            queue = deque()
            queue.append(start)
            visited.add(start)
            while queue:
                cr, cc = queue.pop()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if is_valid(nr, nc):
                        
                        queue.append((nr, nc))
                        visited.add((nr, nc))
           
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] == "1":
                    bfs((i, j), visited)
                    count += 1

        return count