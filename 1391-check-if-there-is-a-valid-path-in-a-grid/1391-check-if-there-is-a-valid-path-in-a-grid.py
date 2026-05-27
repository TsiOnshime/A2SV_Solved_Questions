class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        streets = {
            1: {(0, 1), (0, -1)},
            2: {(1, 0), (-1, 0)},
            3: {(0, -1), (1, 0)},
            4: {(0, 1), (1, 0)},
            5: {(0, -1), (-1, 0)},
            6: {(0, 1), (-1, 0)}
        }

        path = set()


        def is_valid(r, c, needed):
            if r < 0 or c < 0 or c >= cols or r >= rows or (r, c) in path:
                return False
            if needed is None:
                return True

            return needed in streets[grid[r][c]]



        def dfs(r, c, needed):

            if not is_valid(r, c, needed):
                return 
            if r == rows - 1 and c == cols - 1:
                return True

            path.add((r, c))
            for dr, dc in streets[grid[r][c]]:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, (-dr, -dc)):
                    return True
            path.remove((r, c))
        
        if dfs(0, 0, None):
            return True

        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna