class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        pacific = set()
        atlantic = set()
        res = []

        def is_valid(neigh, parent, visited):
            nr, nc = neigh
            cr, cc = parent
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[nr][nc] >= heights[cr][cc]:
                return True
            return False
        def bfs(r, c, visited):
            if (r, c) in visited:
                return 
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + cr, dc + cc
                    if is_valid((nr,nc), (cr, cc), visited):
                        queue.append((nr,nc))
                        visited.add((nr, nc))

        for c in range(cols):
            bfs(0, c, pacific)
            bfs(rows - 1, c, atlantic)
        for r in range(rows):
            bfs(r, 0, pacific)
            bfs(r, cols - 1, atlantic)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res