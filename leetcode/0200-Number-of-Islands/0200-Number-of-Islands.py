class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()
        count = 0
        
        def explore(grid, start, visited):
            r, c = start
            rowInbounds = 0 <= r and r < self.rows
            colsInbounds = 0 <= c and c < self.cols

            if not rowInbounds or not colsInbounds:
                return False
            if grid[r][c] == "0":
                return False
            if start in self.visited:
                return False
            self.visited.add(start)

            explore(grid, (r - 1, c), self.visited)
            explore(grid, (r + 1, c), self.visited)
            explore(grid, (r, c - 1), self.visited)
            explore(grid, (r, c + 1), self.visited)

            return True


        for r in range(self.rows):
            for c in range(self.cols):
                if explore(grid, (r, c), self.visited):
                    count += 1
                
        return count