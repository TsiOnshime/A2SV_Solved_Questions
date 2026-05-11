class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if not 0 <= r < rows or not 0 <= c < cols or (r, c) in visited or grid[r][c] == 0:
                return 
            visited.add(tuple([r, c]))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for i in range(cols):
            dfs(0, i)
            dfs(rows - 1, i)

        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    count += 1

        return count