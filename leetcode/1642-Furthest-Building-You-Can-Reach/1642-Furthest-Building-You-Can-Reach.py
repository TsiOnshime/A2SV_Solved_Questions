class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = [] # top k highest jumps for which we use ladders
        n = len(heights)
        for i in range(n - 1):
            first, second = heights[i], heights[i + 1]
            diff = second - first
            if diff <= 0:
                continue
            else:
                if len(min_heap) < ladders:
                    heapq.heappush(min_heap, diff)
                else:
                    min_height = min_heap[0] if min_heap else 0
                    if diff >= min_height and min_heap:
                        if min_height <= bricks:
                            bricks -= min_height
                            heapq.heappop(min_heap)
                            heapq.heappush(min_heap, diff)
                        else:
                            return i
                    else:
                        if diff <= bricks:
                            bricks -= diff
                        else:
                            return i

        return n - 1