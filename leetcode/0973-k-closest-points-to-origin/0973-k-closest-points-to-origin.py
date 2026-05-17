class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for i in range(len(points)):
            x, y = points[i]
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, [-dist, points[i]])
            if len(heap) > k:
                heapq.heappop(heap)

        for pt in heap:
            res.append(pt[1])

        return res

        



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna