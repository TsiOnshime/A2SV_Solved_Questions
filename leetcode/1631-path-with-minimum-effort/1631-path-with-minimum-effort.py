import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def is_valid(r, c):
            if 0 <= r < rows and 0 <= c < cols:
                return True
            return False

        min_heap = []
        heapq.heappush(min_heap, [0, [0, 0]])

        distance = [[float('inf')] * cols for _ in range(rows)]
        distance[0][0] = 0

        while min_heap:
            diff, cell = heapq.heappop(min_heap)
            r, c = cell
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc):
                    max_diff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                    if max_diff < distance[nr][nc]:
                        heapq.heappush(min_heap, [max_diff, [nr,nc]])
                        distance[nr][nc] = max_diff
        return distance[rows - 1][cols - 1]





            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna