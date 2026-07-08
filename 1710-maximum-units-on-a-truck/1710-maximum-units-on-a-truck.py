class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        max_unit = 0
        heap = [[-units, boxes] for boxes, units in boxTypes]
        heapq.heapify(heap)

        while heap and truckSize:
            units, boxes = heapq.heappop(heap)

            if boxes <= truckSize:
                max_unit += (-units * boxes)
                truckSize -= boxes
            else:
                max_unit += (-units * truckSize)
                truckSize = 0
        return max_unit

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna