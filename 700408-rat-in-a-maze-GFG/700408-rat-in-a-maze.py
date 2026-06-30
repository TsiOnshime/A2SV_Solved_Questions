class Solution:
    def ratInMaze(self, maze):
        # code here
        n = len(maze)
        res = []
        directions = [[1,0, "D"],[0, -1, "L"],[0,1, "R"],[-1, 0, "U"]]
        visited = set()
        if maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
            return []
        visited.add((0, 0))
        def is_valid(r, c):
            if 0 <= r < n and 0 <= c < n and maze[r][c] == 1 and (r, c) not in visited:
                return True
            return False
        def mazePath(r, c, state):
            if r == n - 1 and c == n - 1:
                res.append("".join(state))
                return 
            
            
            for dr, dc, dir in directions:
                cr, cc = r + dr, c + dc
                if is_valid(cr, cc):
                    state.append(dir)
                    visited.add((cr, cc))
                    mazePath(cr, cc, state)
                    state.pop()
                    visited.remove((cr, cc))
                    
        mazePath(0, 0, [])
        return res
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna