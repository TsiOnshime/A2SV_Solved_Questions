class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or board[r][c] == "X" or (r, c) in visited:
                return 
            
            visited.add((r, c))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"
                    


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna