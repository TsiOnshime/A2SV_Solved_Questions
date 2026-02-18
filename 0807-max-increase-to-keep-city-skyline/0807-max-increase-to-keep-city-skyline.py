class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        _sum = 0
        row_max = 0
        col_max = 0

        row = len(grid)
        col = len(grid[0])

        gridNew = [[0 for i in range(row)]for i in range(col)]

        for r in range(row):
            for c in range(col):
                row_max = max(grid[r][0:col])
                
                col_max = max(list(grid[i][c] for i in range(row)))
                
                min_height = min(row_max, col_max)
                gridNew[r][c] = min_height

                _sum += (gridNew[r][c] - grid[r][c])

        return _sum
               
     
        

