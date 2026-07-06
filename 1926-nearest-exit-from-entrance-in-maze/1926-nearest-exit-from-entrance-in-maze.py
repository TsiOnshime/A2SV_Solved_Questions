class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque()
        visited = set()

        queue.append([entrance[0], entrance[1], 0])
        visited.add((entrance[0], entrance[1]))

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def is_valid(r, c):
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and maze[r][c] == ".":
                return True
            return False

        while queue:
   
            r, c, steps = queue.popleft()

            if (r != entrance[0] or c != entrance[1]) and (r == rows - 1 or r == 0 or c == 0 or c == cols - 1):
                return steps
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc):
                    queue.append([nr, nc, steps + 1])
                    visited.add((nr, nc))
        return -1
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna