class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(-1, 0),(1, 0), (0, -1), (0, 1)]
        queue = deque()
        dist = [[float('inf')] * cols for i in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))

        while queue:
            cr, cc= queue.popleft()

            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if nr not in range(rows) or nc not in range(cols):
                    continue
                if dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[cr][cc] + 1
                    queue.append((nr, nc))
        
        return dist