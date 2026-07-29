class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        rows, cols = len(mat), len(mat[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        distance = [[0] * cols for _ in range(rows)]
        visited = [[0] * cols for _ in range(rows)]

        def is_valid(r, c):
            if 0 <= r < rows and 0 <= c < cols and visited[r][c] != 1:
                return True
            return False

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append([(r, c), 0])
                    visited[r][c] = 1
        

        while queue:
            node, dist = queue.popleft()
            r, c = node
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if is_valid(nr, nc):
                    distance[nr][nc] = dist + 1
                    visited[nr][nc] = 1
                    queue.append([(nr, nc), dist + 1])

        return distance






# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna