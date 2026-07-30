class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        distance = [[0] * cols for _ in range(rows)]
        queue = deque()
        visited = set()

        def is_valid(r, c):
            if 0 <= r < rows and 0 <= c < cols and isWater[r][c] == 0 and (r, c) not in visited:
                return True
            return False

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    queue.append([(r, c), 0])
                    visited.add((r, c))

        while queue:
            node, dist = queue.popleft()
            r, c = node
            distance[r][c] = dist
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if is_valid(nr, nc):
                
                    queue.append([(nr, nc), dist + 1])
                    visited.add((nr, nc))
        
        return distance

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna