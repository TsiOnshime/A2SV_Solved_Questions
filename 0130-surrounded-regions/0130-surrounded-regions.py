class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        rows, cols = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        
        def is_valid(r, c):
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and board[r][c] == "O":
                return True
            return False
        def bfs(r, c):
            if board[r][c] != "O" or (r, c) in visited:
                return
            
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if is_valid(nr, nc):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        for c in range(cols):
            bfs(0, c)
            bfs(rows - 1, c)
        for r in range(rows):
            bfs(r, 0)
            bfs(r, cols -1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"
        return board