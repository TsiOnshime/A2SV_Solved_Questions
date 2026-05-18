class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        for i in range(len(points)):
            x, y = points[i]
            dist = (x**2) + (y**2)
            if len(heap) < k:
                heapq.heappush(heap, (-dist, x, y))
            else:
                heapq.heappushpop(heap, (-dist, x, y))

        return [[x, y] for dist, x, y in heap]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna