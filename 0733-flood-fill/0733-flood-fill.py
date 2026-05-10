class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original = image[sr][sc]
        queue = deque()
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def is_valid(r, c):
            if r in range(rows) and c in range(cols) and image[r][c] == original and (r, c) not in visited:
                return True
            return False
        queue.append((sr, sc))
        visited.add((sr, sc))

        while queue:
            cr, cc = queue.popleft()
            image[cr][cc] = color
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if is_valid(nr, nc):
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        return image




