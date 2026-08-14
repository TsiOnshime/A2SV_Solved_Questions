class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        visited = set()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def is_valid(r, c):
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and board[r][c] == "O":
                 return True
            return False

        def bfs(r, c):
            if board[r][c] == "X":
                return 
            if (r, c) in visited:
                return 
            queue = deque()
            queue.append([r, c])
            visited.add((r, c))

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if is_valid(nr, nc):
                        queue.append([nr, nc])
                        visited.add((nr, nc))

        for c in range(cols):
            bfs(0, c)
            bfs(rows - 1, c)
        
        for r in range(rows):
            bfs(r, 0)
            bfs(r, cols - 1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna