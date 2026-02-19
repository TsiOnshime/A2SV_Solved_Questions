class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] < 0:
                    count += 1
        return count
        