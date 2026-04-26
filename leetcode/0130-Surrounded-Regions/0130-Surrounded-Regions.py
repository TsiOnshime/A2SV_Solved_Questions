class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(r, c):
            rowInbounds = 0 <= r and r < rows
            colInbounds = 0 <= c and c < cols
            if not rowInbounds or not colInbounds:
                return
            if board[r][c] == "X":
                return 
            if (r, c) in visited:
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
                if (r, c) not in visited and board[r][c] == "O":
                    board[r][c] = "X"