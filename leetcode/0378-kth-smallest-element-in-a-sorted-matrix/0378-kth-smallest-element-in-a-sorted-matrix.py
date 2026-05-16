class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        max_heap = []
            
            

        for r in range(rows):
            for c in range(cols):
                heapq.heappush_max(max_heap, matrix[r][c])
                if len(max_heap) > k:
                    heapq.heappop_max(max_heap)

        return max_heap[0]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna