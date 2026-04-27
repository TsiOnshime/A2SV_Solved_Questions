class Solution:
    def pacificAtlantic(self, heights):
    
        res = []
        rows = len(heights)
        cols = len(heights[0])
        def dfs(start, pacific, atlantic, visited):
            r,c = start
            if r == 0 or c == 0:
                pacific = True
            if r == rows - 1 or c == cols - 1:
                atlantic = True
            if pacific and atlantic:
                return True, True
            
            if start in visited:
                return pacific, atlantic

            visited.add(start)
            if r - 1 in range(rows) and heights[r-1][c] <= heights[r][c]:
                p,a = dfs((r - 1, c), pacific, atlantic, visited)
                pacific = pacific or p
                atlantic = atlantic or a
            if r + 1 in range(rows) and heights[r + 1][c] <= heights[r][c]:
                p, a = dfs((r + 1, c), pacific, atlantic, visited)
                pacific = pacific or p
                atlantic = atlantic or a
            if c - 1 in range(cols) and heights[r][c - 1] <= heights[r][c]:
                p, a = dfs((r, c - 1), pacific, atlantic, visited)
                pacific = pacific or p
                atlantic = atlantic or a
            if c + 1 in range(cols) and heights[r][c + 1] <= heights[r][c]:
                p, a = dfs((r, c + 1), pacific, atlantic, visited)
                pacific = pacific or p
                atlantic = atlantic or a
            
            return pacific, atlantic


        for r in range(rows):
            for c in range(cols):
                pacific = atlantic = False
                visited = set()
                pacific, atlantic = dfs((r,c), pacific, atlantic, visited)
                if pacific and atlantic:
                    res.append([r,c])

        return res

o = Solution()
print(o.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))