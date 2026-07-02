class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_gold = 0
        visited = set()

        def is_valid(r, c):
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] != 0:
                return True
            return False

        def dfs(r, c):

            if not is_valid(r, c):
                return 0
            
            gold = grid[r][c]

            visited.add((r, c))
            
            gold += max(dfs(r + 1, c), dfs(r - 1, c), dfs(r, c + 1), dfs(r, c - 1))

            visited.remove((r, c))
            return gold







        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    max_gold = max(dfs(r, c), max_gold)

        
        return max_gold




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna